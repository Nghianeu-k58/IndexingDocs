"""
Define all test file.
"""

from src.rag.file.models import DocsIndexingFields
from src.rag.file.utils import (
    preparing_index_document,
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

    assert DocsIndexingFields.id in func_out
    assert DocsIndexingFields.content in func_out
    assert DocsIndexingFields.created_date in func_out
    assert DocsIndexingFields.user in func_out
    assert DocsIndexingFields.title in func_out
    assert DocsIndexingFields.key_words in func_out
