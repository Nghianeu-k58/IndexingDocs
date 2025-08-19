"""
Define all logic for API endpoint.
"""

import os
from datetime import datetime, timedelta, timezone

from fastapi import Depends
from fastapi.security.api_key import APIKeyHeader
from passlib.context import CryptContext
from elasticsearch import Elasticsearch
from jose import jwt

from src.rag.core.enums import SystemENV, DATETIME_FORMAT
from src.rag.core.logger import logger
from src.rag.dataaccess.configuration.elasticsearch.enums import ElasticsearchIndies
from src.rag.auth.enums import UserInfo, TokenFields

# from src.rag.core.logger import logger

# ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 1

api_key_header = APIKeyHeader(name="LocalRagAPIKey", auto_error=False)
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def validate_api_key(api_key_header: str = Depends(api_key_header)):
    """Validate api key header."""
    if api_key_header == os.environ.get(SystemENV.api_key):
        return True
    return False


def check_user_in_db(user: dict, es_conn: Elasticsearch):
    """Check and user in db or not."""
    logger.info(f"Authenticate user with email: {user[UserInfo.email]}")
    result = es_conn.search(
        index=ElasticsearchIndies.user,
        body={"query": {"match": {"email": user[UserInfo.email]}}},
    )

    user_search = result["hits"]["hits"]
    logger.debug(f"Check user search {user_search}")
    if len(user_search) == 0:
        return None, "Email or password are incorrect. Please try again ..."

    # check password
    user_detail = user_search[0]["_source"]

    if not bcrypt_context.verify(
        user[UserInfo.password],
        user_detail[UserInfo.password],
    ):
        return None, "Email or password are incorrect. Please try again ..."

    return user_detail, "OK"


def create_access_token(
    email: str,
    user_id: str,
    role: str,
):
    """Create and return access token."""
    encode = {
        TokenFields.email: email,
        TokenFields.user_id: user_id,
        TokenFields.role: role,
    }
    token = jwt.encode(
        claims=encode,
        key=os.environ.get(SystemENV.secret_key),
        algorithm=os.environ.get(SystemENV.algorithm),
    )
    expires = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    return token, expires.strftime(DATETIME_FORMAT)
