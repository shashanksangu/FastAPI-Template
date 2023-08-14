from typing import Dict, Optional, Any
from fastapi import FastAPI, File, UploadFile, Request, status, APIRouter, Query

api_version = "init"

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/"+api_version,
    tags=[api_version],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"message": "FastAPI - Version - "+api_version}

