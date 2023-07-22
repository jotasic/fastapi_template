from app.api.v1.endpoints import items
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
