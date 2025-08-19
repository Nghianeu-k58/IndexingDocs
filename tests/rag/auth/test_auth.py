"""
Test all auth services.
"""
import os


import pytest
from fastapi import status

from src.rag.auth.services import validate_api_key
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
