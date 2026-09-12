import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import text

from src.backend.app import create_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    url = f"sqlite:///{tmp_path / 'test.db'}"
    monkeypatch.setenv("DATABASE_URL", url)
    command.upgrade(Config("alembic.ini"), "head")
    app = create_app(url, static_dir=tmp_path / "no-frontend")
    with app.state.engine.begin() as conn:
        conn.execute(text("INSERT INTO categories (id, name) VALUES (1, 'Books')"))
    with TestClient(app) as result:
        yield result
    app.state.engine.dispose()


def test_empty_and_create_read(client):
    assert client.get("/api/items").json() == []
    created = client.post("/api/items", json={"name": "Atlas", "category_id": 1})
    assert created.status_code == 201
    assert client.get(f"/api/items/{created.json()['id']}").json()["name"] == "Atlas"
    assert len(client.get("/api/items").json()) == 1


@pytest.mark.parametrize("payload", [{}, {"name": " ", "category_id": 1},
                                   {"name": "x", "category_id": 99},
                                   {"name": "x", "category_id": 0}])
def test_invalid_input(client, payload):
    assert client.post("/api/items", json=payload).status_code == 422
    assert client.get("/api/items").json() == []


def test_duplicate_conflict_does_not_poison_session(client):
    body = {"name": "Atlas", "category_id": 1}
    assert client.post("/api/items", json=body).status_code == 201
    assert client.post("/api/items", json=body).status_code == 409
    assert client.post("/api/items", json={**body, "name": "Map"}).status_code == 201


def test_missing_and_bounds(client):
    assert client.get("/api/items/999").status_code == 404
    assert client.get("/api/items?limit=101").status_code == 422
    assert client.get("/api/health").json() == {"status": "ok"}
    assert client.get("/api/categories").json() == [{"id": 1, "name": "Books"}]


def test_foreign_key_enforced(client):
    from sqlalchemy.exc import IntegrityError
    with pytest.raises(IntegrityError), client.app.state.engine.begin() as conn:
        conn.execute(text("INSERT INTO items (name, category_id) VALUES ('bad', 999)"))


def test_built_frontend_serving(tmp_path):
    (tmp_path / "index.html").write_text("<h1>CAP</h1>")
    app = create_app(f"sqlite:///{tmp_path / 'web.db'}", static_dir=tmp_path)
    with TestClient(app) as client:
        assert "CAP" in client.get("/").text
        assert client.get("/api/health").status_code == 200
    app.state.engine.dispose()


def test_seed_is_repeatable(client):
    from src.backend.seed import main
    with client.app.state.engine.begin() as conn:
        conn.execute(text("DELETE FROM categories"))
    main()
    main()
    assert len(client.get("/api/categories").json()) == 1
