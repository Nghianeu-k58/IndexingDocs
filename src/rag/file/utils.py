"""
Define all helper functions for file processsing
"""

from datetime import datetime

from src.rag.core.enums import DATETIME_FORMAT, HashAlgorithms
from src.rag.file.models import DocsIndexingFields
from src.rag.core.utils import generate_id


def preparing_index_document(
    key_words: list,
    doc_content: str,
    title: str,
    user: str,
):
    """Create and return indexing document."""
    created_date = datetime.now().strftime(DATETIME_FORMAT)
    doc_id = generate_id(HashAlgorithms.md5, title, created_date, user)

    return {
        DocsIndexingFields.doc_id: doc_id,
        DocsIndexingFields.doc_content: doc_content,
        DocsIndexingFields.keywords: key_words,
        DocsIndexingFields.insert_user: user,
        DocsIndexingFields.title: title,
        DocsIndexingFields.created_date: created_date,
    }
