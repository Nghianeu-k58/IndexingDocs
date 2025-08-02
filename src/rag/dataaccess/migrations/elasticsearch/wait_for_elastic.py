"""
Define the function waiting for ElasticSearch database.
"""
import os
import time

import requests
from requests.exceptions import ConnectionError as RequestsConnectionError
from elasticsearch.exceptions import ConnectionError as ElasticConnectionError

from src.rag.core.logger import logger
from src.rag.core.enums import ElasticENV

ELASTIC_HOST = os.environ.get(ElasticENV.host)
ELASTIC_PORT = os.environ.get(ElasticENV.port)

URL = f"http://{ELASTIC_HOST}:{ELASTIC_PORT}/_cluster/health"


def wait_for_elastic_search():
    logger.info("Start waitting for ElasticSearch dabase ready ...")
    elastic_ready = False

    while elastic_ready is False:
        try:
            requests.get(url=URL)
            logger.info("ElasticSearch is ready.")
            elastic_ready = True
        except (ElasticConnectionError, RequestsConnectionError):
            logger.info("ElasticSearch is not ready. Wait for 5 seconds ...")
            time.sleep(5)


if __name__ == "__main__":
    wait_for_elastic_search()
