"""
Define all API endpoint for user.
"""

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from elasticsearch import Elasticsearch

from src.rag.user.models import UserCreate
from src.rag.dataaccess.migrations.elasticsearch.connection import (
    get_elastic_connection,
)
from src.rag.user.services import create_user_logic


router = APIRouter(prefix="/users", tags=["User"])


@router.post("/")
def create_user(
    user_data: UserCreate,
    db: Elasticsearch = Depends(get_elastic_connection),
):
    """Endpoint of create user."""
    res, msg = create_user_logic(
        user_data.model_dump(),
        es_conn=db,
    )

    if not res:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"msg": msg}
        )
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"msg": msg})
