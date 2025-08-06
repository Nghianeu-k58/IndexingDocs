"""
Define router uploading file to indexing to database.
"""

from fastapi import (
    APIRouter,
    # status,
    # Depends,
    # Form,
)

# from fastapi.responses import JSONResponse

router = APIRouter(prefix="/files", tags=["Files"])
