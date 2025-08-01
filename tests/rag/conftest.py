"""
Define all support for test
"""

import pytest
from fastapi.testclient import TestClient
from src.rag.main import app


@pytest.fixture(scope="function")
def client():
    """Create and return a mock client."""
    yield TestClient(app)
