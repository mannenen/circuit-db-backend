import pytest

from starlette.testclient import TestClient

from backend.main import app
from backend.database.mongo import MongoDatabase


@pytest.fixture
def db(mongodb):
    yield MongoDatabase(mongodb)


@pytest.fixture
def test_client(db):
    app.state.db = db
    yield TestClient(app)
