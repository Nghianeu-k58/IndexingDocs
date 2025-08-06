"""
Define all support for test
"""
import os

import pytest
from fastapi.testclient import TestClient
from elasticsearch import Elasticsearch

# from elasticsearch.helpers import bulk

from src.rag.main import app
from src.rag.core.enums import ElasticENV
from src.rag.dataaccess.migrations.elasticsearch.connection import (
    get_elastic_connection,
)
from src.rag.dataaccess.migrations.elasticsearch.enums import ElasticsearchIndies
from src.rag.user.enums import UserField, Role

ELASTIC_HOST = os.environ.get(ElasticENV.host)
ELASTIC_PORT = int(os.environ.get(ElasticENV.port))
ELASTIC_ENDPOINT = f"{ELASTIC_HOST}:{ELASTIC_PORT}"
TEST_ELASTIC_USERNAME = os.environ.get(ElasticENV.user_name)
TEST_ELASTIC_PASSWORD = os.environ.get(ElasticENV.password)
TEST_ELASTIC_VERIFY_CERTS = os.environ.get(ElasticENV.verify_certs)
TEST_ELASTIC_SCHEME_CONNNECTION = os.environ.get(ElasticENV.connection_scheme)


ELASTIC_HOST_FAKE = "fake_elastic_host"
ELASTIC_PORT_FAKE = 1234

os.environ[ElasticENV.host] = ELASTIC_HOST_FAKE
os.environ[ElasticENV.port] = str(ELASTIC_PORT_FAKE)


@pytest.fixture(scope="session")
def es_connection():
    conn = Elasticsearch(
        hosts=[
            {
                "host": ELASTIC_HOST,
                "port": ELASTIC_PORT,
                "scheme": TEST_ELASTIC_SCHEME_CONNNECTION,
            },
        ],
        basic_auth=tuple([TEST_ELASTIC_USERNAME, TEST_ELASTIC_PASSWORD]),
        verify_certs=bool(TEST_ELASTIC_VERIFY_CERTS),
    )
    try:
        yield conn
    finally:
        indices = conn.indices.get_alias(index="*").keys()
        for idx in indices:
            if idx.startswith("."):  # skip system indices
                continue
            conn.delete_by_query(index=idx, body={"query": {"match_all": {}}})
        conn.close()


@pytest.fixture(scope="function")
def client(es_connection):
    """Create and return a mock client."""

    def overwrite_es_conn():
        yield es_connection

    app.dependency_overrides[get_elastic_connection] = overwrite_es_conn
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides[get_elastic_connection] = get_elastic_connection


@pytest.fixture()
def users_data(es_connection):
    records = [
        {
            UserField.user_id: f"Testidforuser{i}",
            UserField.email: f"test_example{i}.com",
            UserField.password: "Testpass-123",
            UserField.name: f"Test name {i}",
            UserField.role: Role.user,
            UserField.created_date: "2025-01-01",
        }
        for i in range(2)
    ]

    for record in records:
        es_connection.index(
            index=ElasticsearchIndies.user,
            document=record,
        )

    es_connection.indices.refresh(index=ElasticsearchIndies.user)
    yield records
