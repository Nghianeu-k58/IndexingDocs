"""
Managing all API router registers.
"""

from fastapi import APIRouter

from src.rag.auth.views import router as auth_router
from src.rag.file.views import router as file_router
from src.rag.user.views import router as user_router

api_routers = APIRouter(prefix="/api/v1")
api_routers.include_router(auth_router)
api_routers.include_router(file_router)
api_routers.include_router(user_router)
