"""
Define all logic for API endpoint.
"""

import os

from fastapi import Depends
from fastapi.security.api_key import APIKeyHeader
from passlib.context import CryptContext

from src.rag.core.enums import SystemENV

# from src.rag.core.logger import logger

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 11

api_key_header = APIKeyHeader(name="LocalRagAPIKey", auto_error=False)
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def authenticate_user(email: str, password: str, db: Session) -> (object, str):
#     """Authenticating user and return result."""
#     # query user in db by email
#     logger.info(f"Authenticate user with email: {email}")
#     user = db.query(models.User).where(models.User.email == email).first()

#     if not user:
#         return None, "Email or password are incorrect. Please try again ..."

#     logger.debug(f"User: {user.email} - {user.org_id} - {user.name}")
#     # check password
#     if not bcrypt_context.verify(password, user.password):
#         return None, "Email or password are incorrect. Please try again ..."

#     return user, "OK"


async def validate_api_key(api_key_header: str = Depends(api_key_header)):
    """Validate api key header."""
    if api_key_header == os.environ.get(SystemENV.api_key):
        return True
    return False
