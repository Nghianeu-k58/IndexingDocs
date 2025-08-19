"""
Define all pydantic models for authenticate
"""

from pydantic import BaseModel, SecretStr, Field


class UserBase(BaseModel):
    email: str
    password: SecretStr = Field(
        json_schema_extra={
            "title": "Password",
            "description": "User's secret password",
            "examples": ["SecurePassword123!"],
            "format": "password",  # Helps with schema generation for UI/API tools
            "writeOnly": True,  # Indicates it's for input, not output
        }
    )
