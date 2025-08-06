"""
Define all test file.
"""

from src.rag.file.models import DocsIndexingFields
from src.rag.file.utils import (
    preparing_index_document,
    generate_doc_id,
)
from src.rag.user.enums import Role


def test_preparing_index_document():
    """Test preparing index doc."""
    func_out = preparing_index_document(
        key_words=["test_key1"],
        doc_content="This is doc content.",
        title="Test title.",
        user=Role.anonymous,
    )

    assert DocsIndexingFields.doc_id in func_out
    assert DocsIndexingFields.doc_content in func_out
    assert DocsIndexingFields.created_date in func_out
    assert DocsIndexingFields.insert_user in func_out
    assert DocsIndexingFields.keywords in func_out


def test_generate_doc_id():
    expected_hash = "550d127505408bd07563de346c99d354"
    func_out = generate_doc_id(
        user=Role.anonymous,
        title="Test_title",
        created_date="2025/08/04",
    )

    assert expected_hash == func_out
