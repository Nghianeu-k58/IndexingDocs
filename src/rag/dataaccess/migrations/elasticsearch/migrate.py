"""
Migrate data schemas in ElasticSearch
"""

import os
import json
import sys

from elasticsearch import Elasticsearch

from src.rag.core.logger import logger
from src.rag.core.enums import ElasticENV
from src.rag.dataaccess.migrations.elasticsearch.connection import es_conn

MAPPING_VERSION = os.environ.get(ElasticENV.mapping_version)
mapping_file = (
    f"src/rag/dataaccess/migrations/elasticsearch/{MAPPING_VERSION}.mapping.json"
)


def main(es_conn: Elasticsearch):
    """Starting migrate process."""

    logger.info("Check mappping file ...")
    if not os.path.exists(mapping_file):
        logger.warning(f"Cannot found mapping file at {mapping_file}.")
        sys.exit(1)

    with open(mapping_file, mode="r", encoding="utf-8") as f:
        schemas = json.load(f)

    logger.info("Start migration for Elasticsearch ...")
    for table_name, fields in schemas.items():
        if es_conn.indices.exists(index=f"{table_name}_{MAPPING_VERSION}"):
            continue
        es_conn.indices.create(
            index=f"{table_name}_{MAPPING_VERSION}",
            body=fields,
        )

    logger.info(f"Migrate completed with mapping version {MAPPING_VERSION}")


if __name__ == "__main__":
    main(es_conn)
