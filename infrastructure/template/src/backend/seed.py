from sqlalchemy import select
from sqlalchemy.orm import Session

from .app import make_engine
import os
from .models import Category


def main():
    engine = make_engine(os.getenv("DATABASE_URL", "sqlite:///./cap.db"))
    with Session(engine) as db:
        if db.scalar(select(Category).where(Category.name == "Books")) is None:
            db.add(Category(name="Books"))
            db.commit()
    engine.dispose()


if __name__ == "__main__":
    main()
