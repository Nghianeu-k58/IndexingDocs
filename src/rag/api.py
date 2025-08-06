"""
Managing all API router registers.
"""

from fastapi import APIRouter

from src.rag.file.views import router as file_router

api_routers = APIRouter(prefix="/api/v1")
api_routers.include_router(file_router)
