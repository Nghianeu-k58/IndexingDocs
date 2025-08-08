"""
Define all pydantic models.
"""

from pydantic import BaseModel
from typing import List


class DocsIndexingFields:
    id = "doc_id"
    key_words = "key_words"
    content = "doc_content"
    created_date = "created_date"
    title = "title"
    user = "insert_user"


# Define all Pydantic model.


class BaseDocs(BaseModel):
    doc_id: str


class DocsInsert(BaseModel):
    title: str
    key_words: List[str]
