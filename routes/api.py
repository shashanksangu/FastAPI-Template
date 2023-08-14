from fastapi import APIRouter
from src.endpoints import init
from src.endpoints import v1

router = APIRouter()
router.include_router(init.router)
router.include_router(v1.router)
