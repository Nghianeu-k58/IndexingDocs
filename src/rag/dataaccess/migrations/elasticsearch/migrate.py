"""
Migrate data schemas in ElasticSearch
"""

import os
import json
import sys

from elasticsearch import Elasticsearch

from src.rag.core.logger import logger
from src.rag.core.enums import ElasticENV
from rag.dataaccess.configuration.elasticsearch.connection import (
    preparing_connection_to_es,
)

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
        if es_conn.indices.exists(index=f"{table_name}"):
            mappings = es_conn.indices.get_mapping(index=table_name)
            current_version = (
                mappings.get(table_name, {})
                .get("mappings", {})
                .get("_meta", {})
                .get("mapping_version", {})
            )
            if current_version == MAPPING_VERSION:
                continue

        es_conn.indices.create(
            index=f"{table_name}",
            body=fields,
        )

    logger.info(f"Migrate completed with mapping version {MAPPING_VERSION}")


if __name__ == "__main__":
    es_conn = preparing_connection_to_es()
    main(es_conn)
