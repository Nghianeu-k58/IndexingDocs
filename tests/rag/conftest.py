"""
Define all support for test
"""
import os
import pytest
from fastapi.testclient import TestClient

from src.rag.main import app
from src.rag.core.enums import ElasticENV


ELASTIC_HOST_FAKE = "fake_elastic_host"
ELASTIC_PORT_FAKE = 1234

os.environ[ElasticENV.host] = ELASTIC_HOST_FAKE
os.environ[ElasticENV.port] = str(ELASTIC_PORT_FAKE)


@pytest.fixture(scope="function")
def client():
    """Create and return a mock client."""
    yield TestClient(app)
