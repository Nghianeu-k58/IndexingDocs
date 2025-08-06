"""
Define all pydantic model for user.
"""

from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str
    name: str


class UserBase(BaseModel):
    use_id: str
