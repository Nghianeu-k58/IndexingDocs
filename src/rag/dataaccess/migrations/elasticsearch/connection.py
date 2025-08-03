"""
Define connection of elasticsearch
"""

import os

from elasticsearch import Elasticsearch

from src.rag.core.logger import logger
from src.rag.core.enums import ElasticENV


ELASTIC_HOST = os.environ.get(ElasticENV.host)
ELASTIC_PORT = int(os.environ.get(ElasticENV.port))
ELASTIC_ENDPOINT = f"{ELASTIC_HOST}:{ELASTIC_PORT}"
ELASTIC_USERNAME = os.environ.get(ElasticENV.user_name)
ELASTIC_PASSWORD = os.environ.get(ElasticENV.password)
ELASTIC_VERIFY_CERTS = os.environ.get(ElasticENV.verify_certs)
ELASTIC_SCHEME_CONNNECTION = os.environ.get(ElasticENV.connection_scheme)


logger.debug(f"Connect to ElasticSearch database at {ELASTIC_ENDPOINT}")


es_conn = Elasticsearch(
    hosts=[
        {
            "host": ELASTIC_HOST,
            "port": ELASTIC_PORT,
            "scheme": ELASTIC_SCHEME_CONNNECTION,
        },
    ],
    http_auth=tuple([ELASTIC_USERNAME, ELASTIC_PASSWORD]),
    verify_certs=bool(ELASTIC_VERIFY_CERTS),
)


def get_elastic_connection():
    """Get and return ELASTIC connection."""
    yield es_conn
