"""
Define all endpoint for authenticate.
"""

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from elasticsearch import Elasticsearch

from src.rag.auth.models import UserBase
from src.rag.auth.enums import UserInfo
from src.rag.dataaccess.configuration.elasticsearch.connection import (
    get_elastic_connection,
)
from src.rag.auth.services import check_user_in_db

router = APIRouter(prefix="/auth", tags=["Authentication"])
# user_dependency = Annotated[dict, Depends(get_current_user_via_token)]


@router.post("/login")
def login(user: UserBase, es_conn: Elasticsearch = Depends(get_elastic_connection)):
    """Login for user."""

    user_info = {
        UserInfo.email: user.email,
        UserInfo.password: user.password.get_secret_value(),
    }

    result, msg = check_user_in_db(user=user_info, es_conn=es_conn)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"msg": msg}
        )
    return JSONResponse(status_code=status.HTTP_200_OK, content={"msg": "OK"})
