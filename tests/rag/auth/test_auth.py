"""
Test all auth services.
"""
import os

# from datetime import datetime, timedelta, timezone
# from unittest.mock import patch

import pytest
from src.rag.auth.services import validate_api_key
from src.rag.core.enums import (
    SystemENV,
    # UserFields,
)

os.environ[SystemENV.api_key] = "SuperSecretKey"
os.environ[SystemENV.algorithm] = "HS256"
os.environ[SystemENV.expire_day] = "1"


# @patch("src.ailiver.auth.services.datetime")
# def test_create_access_token(patched_datetime):
#     """Test create access token."""
#     patched_datetime.now.return_value = datetime(
#         year=2023,
#         month=4,
#         day=15,
#         hour=12,
#         minute=0,
#         second=0,
#     )
#     expected_expiry = datetime(
#         year=2023,
#         month=4,
#         day=15,
#         hour=12,
#         minute=0,
#         second=0,
#     ) + timedelta(days=1)

#     user_email = "test_user@example.com"
#     user_id = 1
#     org_id = 1
#     is_superuser = False

#     token_elements = [
#         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
#         "eyJzdWIiOiJ0ZXN0X3VzZXJAZXhhbXBsZS5jb20iLCJpZCI6MSwib3JnX2lkIjoxLCJyb2xlIjpmYWxzZSwiZXhwIjoxNjgxNjQ2NDAwfQ",
#         "Kc7Aq7CcIAnJil54oQ-ZOX7btQoz0wkeglCY3ib2reE",
#     ]

#     expected_token = f"{token_elements[0]}.{token_elements[1]}.{token_elements[2]}"
#     func_out, expiry_date = create_access_token(
#         email=user_email,
#         user_id=user_id,
#         org_id=org_id,
#         role=is_superuser,
#     )

#     patched_datetime.now.assert_called_once_with(timezone.utc)
#     assert expected_token == func_out
#     assert expected_expiry.strftime("%d/%m/%Y - %H:%M:%S") == expiry_date


# def test_authenticate_user_successful(session, users_data):
#     """Test authenticate user successful."""
#     email = "test_user1@example.com"
#     password = "Testpassword-123"

#     expected_msg = "OK"
#     result, msg = authenticate_user(email=email, password=password, db=session)

#     assert result is not None
#     assert expected_msg == msg


# def test_authenticate_user_with_wrong_email(session, users_data):
#     """Test authenticate user successful."""
#     email = "wrong_email@example.com"

#     expected_msg = "Email or password are incorrect. Please try again ..."
#     result, msg = authenticate_user(email=email, password="test123", db=session)

#     assert result is None
#     assert expected_msg == msg


# def test_authenticate_user_with_wrong_password(session, users_data):
#     """Test authenticate user successful."""
#     email = "test_user1@example.com"
#     wrong_password = "Wrong password"

#     expected_msg = "Email or password are incorrect. Please try again ..."
#     result, msg = authenticate_user(email=email, password=wrong_password, db=session)

#     assert result is None
#     assert expected_msg == msg


# @pytest.mark.asyncio
# async def test_get_current_user_via_token_successful():
#     """Test get current user successful."""
#     email = "test_user@example.com"
#     user_id = 1
#     org_id = 1
#     is_superuser = False
#     token, _ = create_access_token(
#         user_id=user_id,
#         email=email,
#         org_id=org_id,
#         role=is_superuser,
#     )

#     user = await get_current_user_via_token(token=token)

#     assert UserFields.email in user
#     assert UserFields.user_id in user
#     assert UserFields.role in user


# @pytest.mark.asyncio
# async def test_get_current_user_via_token_failed():
#     """Test get current user successful."""
#     elements = [
#         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
#         "eyJzdWIiOiJ0ZXN0X3VzZXJAZXhhbXBsZS5jb20iLCJpZCI6MSwiZXhwIjoxNjgxNjQ2NDAwfQ",
#         "cpCWNvrZna0QdSOJ50Bbwz7joaOzmhatzyLe3QHfabc",  # change last to abc
#     ]
#     input_token = f"Bearer {elements[0]}.{elements[1]}.{elements[2]}"

#     user = await get_current_user_via_token(token=input_token)

#     assert user is None


# @pytest.mark.asyncio
# async def test_get_current_user_via_token_error():
#     """Test raise error."""
#     elements = [
#         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
#         "eyJzdWIiOiJ0ZXN0X3VzZXJAZXhhbXBsZS5jb20iLCJpZCI6MSwiZXhwIjoxNjgxNjQ2NDAwfQ",
#         "cpCWNvrZna0QdSOJ50Bbwz7joaOzmhatzyLe3QHfNK8",
#     ]
#     input_token = f"{elements[0]}.{elements[1]}.{elements[2]}abc"
#     user = await get_current_user_via_token(token=input_token)

#     assert user is None


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
