"""
Define all helper functions for file processsing
"""

import hashlib
from datetime import datetime

from src.rag.core.enums import DATETIME_FORMAT
from src.rag.file.models import DocsIndexingFields


def preparing_index_document(
    key_words: list,
    doc_content: str,
    title: str,
    user: str,
):
    """Create and return indexing document."""
    created_date = datetime.now().strftime(DATETIME_FORMAT)
    doc_id = generate_doc_id(title=title, created_date=created_date, user=user)

    return {
        DocsIndexingFields.doc_id: doc_id,
        DocsIndexingFields.doc_content: doc_content,
        DocsIndexingFields.keywords: key_words,
        DocsIndexingFields.insert_user: user,
        DocsIndexingFields.created_date: created_date,
    }


def generate_doc_id(
    title: str,
    created_date: str,
    user: str,
):
    """Generate and return docid."""
    return hashlib.md5(f"{user}{title}{created_date}".encode()).hexdigest()
