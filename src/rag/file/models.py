"""
Define all pydantic models.
"""

from pydantic import BaseModel
from typing import List


class DocsIndexingFields:
    doc_id = "doc_id"
    keywords = "keywords"
    doc_content = "doc_content"
    created_date = "created_date"
    title = "title"
    insert_user = "insert_user"


# Define all Pydantic model.


class BaseDocs(BaseModel):
    doc_id: str
    user: str


class DocsInsert(BaseDocs):
    title: str
    key_words: List[str]
