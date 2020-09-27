import pytest

from starlette.testclient import TestClient

from backend.main import app
from backend.database import MongoDatabase


@pytest.fixture
def test_client():
    yield TestClient(app)


@pytest.fixture
def db(mongodb):
    yield MongoDatabase(mongodb)
