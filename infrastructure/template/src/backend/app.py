import os
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict, Field, field_validator
from sqlalchemy import create_engine, event, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .models import Category, Item


def make_engine(url):
    engine = create_engine(url, connect_args={"check_same_thread": False} if url.startswith("sqlite") else {})
    if url.startswith("sqlite"):
        @event.listens_for(engine, "connect")
        def enable_foreign_keys(connection, _):
            connection.execute("PRAGMA foreign_keys=ON")
    return engine


class ItemInput(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    category_id: int = Field(gt=0)

    @field_validator("name")
    @classmethod
    def nonblank(cls, value):
        if not value.strip():
            raise ValueError("name must not be blank")
        return value.strip()


class ItemOutput(ItemInput):
    model_config = ConfigDict(from_attributes=True)
    id: int


def create_app(database_url=None, static_dir=None):
    app = FastAPI(title="CAP Inventory Reference")
    engine = make_engine(database_url or os.getenv("DATABASE_URL", "sqlite:///./cap.db"))
    app.state.engine = engine

    def session():
        with Session(engine) as db:
            yield db

    @app.get("/api/health")
    def health():
        return {"status": "ok"}

    @app.get("/api/categories")
    def categories(db: Session = Depends(session)):
        return [{"id": c.id, "name": c.name} for c in db.scalars(select(Category).order_by(Category.id))]

    @app.get("/api/items", response_model=list[ItemOutput])
    def items(limit: int = Query(50, ge=1, le=100), db: Session = Depends(session)):
        return list(db.scalars(select(Item).order_by(Item.id).limit(limit)))

    @app.get("/api/items/{item_id}", response_model=ItemOutput)
    def get_item(item_id: int, db: Session = Depends(session)):
        item = db.get(Item, item_id)
        if item is None:
            raise HTTPException(404, "Item not found")
        return item

    @app.post("/api/items", response_model=ItemOutput, status_code=201)
    def create_item(body: ItemInput, db: Session = Depends(session)):
        if db.get(Category, body.category_id) is None:
            raise HTTPException(422, "Unknown category")
        item = Item(**body.model_dump())
        db.add(item)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise HTTPException(409, "Item conflicts with existing data") from None
        db.refresh(item)
        return item

    # Built React assets are served on the same origin after API routes.
    frontend = Path(static_dir or Path(__file__).resolve().parents[1] / "frontend" / "dist")
    if frontend.is_dir():
        app.mount("/", StaticFiles(directory=frontend, html=True), name="frontend")
    return app


app = create_app()
