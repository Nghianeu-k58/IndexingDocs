"""
Define logic for upload file endpoint.
"""
from datetime import datetime

from elasticsearch import Elasticsearch

from src.rag.core.logger import logger
from src.rag.core.utils import generate_id
from src.rag.core.enums import HashAlgorithms
from src.rag.file.models import DocsIndexingFields
from src.rag.dataaccess.migrations.elasticsearch.enums import ElasticsearchIndies
from src.rag.user.enums import Role


def insert_doc(
    doc: dict,
    es_conn: Elasticsearch,
):
    """Insert docs to db."""
    logger.info("Add more fields to doc ...")
    curr_time = datetime.now().isoformat()
    doc[DocsIndexingFields.created_date] = curr_time

    doc_id = generate_id(HashAlgorithms.md5, doc[DocsIndexingFields.title], curr_time)
    doc[DocsIndexingFields.id] = doc_id

    doc[DocsIndexingFields.user] = Role.anonymous

    es_conn.index(
        index=ElasticsearchIndies.documentation,
        document=doc,
    )
    es_conn.indices.refresh(index=ElasticsearchIndies.documentation)

    return True, "OK"
