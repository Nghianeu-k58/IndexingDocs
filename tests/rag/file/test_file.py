"""
Test file API.
"""

from fastapi import status

from src.rag.file.models import DocsIndexingFields
from src.rag.dataaccess.configuration.elasticsearch.enums import ElasticsearchIndies


TEST_FILE_DATA = "tests/rag/file/data/test_doc.txt"
FILE_URL = "/api/v1/files"


def test_insert_docs_to_db_successful(client, es_connection):
    # preparing docs
    doc_insert = {
        DocsIndexingFields.title: "Test title",
        DocsIndexingFields.key_words: ["Keyword1", "Keyword2"],
    }

    with open(TEST_FILE_DATA, mode="rb") as f:
        res = client.post(
            url=FILE_URL,
            data=doc_insert,
            files=[("file", f)],
        )

    assert res.status_code == status.HTTP_200_OK
    assert res.json()["msg"] == "OK"

    doc = es_connection.search(
        index=ElasticsearchIndies.documentation,
        body={"query": {"match": {DocsIndexingFields.title: "Test title"}}},
    )
    assert len(doc["hits"]["hits"]) != 0
