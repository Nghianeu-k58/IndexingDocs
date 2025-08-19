"""
Test all auth services.
"""
import os

from unittest.mock import patch
import pytest
from fastapi import status
from datetime import datetime

from src.rag.auth.services import (
    validate_api_key,
    create_access_token,
)
from src.rag.core.enums import (
    SystemENV,
    # UserFields,
)

os.environ[SystemENV.api_key] = "SuperSecretKey"
os.environ[SystemENV.algorithm] = "HS256"
os.environ[SystemENV.expire_day] = "1"


AUTH_URL = "/api/v1/auth"
LOGIN_URL = f"{AUTH_URL}/login"


def test_login_successful(client, users_data):
    data = {"email": "test_user0@example.com", "password": "Testpass-123"}
    res = client.post(url=LOGIN_URL, json=data)

    assert res.json() is not None
    assert res.status_code == status.HTTP_200_OK


def test_login_with_wrong_password(client, users_data):
    data = {"email": "test_user0@example.com", "password": "wrong password"}
    res = client.post(url=LOGIN_URL, json=data)

    assert res.json()["msg"] == "Email or password are incorrect. Please try again ..."
    assert res.status_code == status.HTTP_400_BAD_REQUEST


def test_login_with_unknow_user(client):
    data = {"email": "unknow_user@example.com", "password": "Testpass-123"}
    res = client.post(url=LOGIN_URL, json=data)

    assert res.json()["msg"] == "Email or password are incorrect. Please try again ..."
    assert res.status_code == status.HTTP_400_BAD_REQUEST


# Functions
@pytest.mark.asyncio
async def test_validate_api_key_successful():
    """Test validate api token successful."""
    input_key = "SuperSecretKey"

    func_out = await validate_api_key(api_key_header=input_key)

    assert func_out is True


@pytest.mark.asyncio
async def test_validate_api_key_failed():
    """Test validate api token failed."""
    input_key = "SuperSecretKeyButWrong"

    func_out = await validate_api_key(api_key_header=input_key)

    assert func_out is False


@patch("src.rag.auth.services.datetime")
def test_create_access_token(patched_time):
    """Test for create access token."""
    patched_time.now.return_value = datetime(2025, 1, 1, 00, 00, 00)

    parts = [
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        "eyJzdWIiOiJ0ZXN0X3VzZXJAZXhhbXBsZS5jb20iLCJpZCI6InRlc3RfdXNlcl9pZCIsInJvbGUiOiJ1c2VyIn0",
        "LGPjkFDKORBVxkuFqpswC_gu2loVRP6Vi-f8QYSXHCQ",
    ]

    token, expires = create_access_token(
        email="test_user@example.com", user_id="test_user_id", role="user"
    )

    assert ".".join(parts) == token
    assert expires == "2025-01-02 00-00-00"
