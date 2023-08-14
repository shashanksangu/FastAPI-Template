import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routes.api import router as api_router

import logging

from ws import app as ws

from pathlib import Path

app = FastAPI()

origins = ["http://localhost:8000", "http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Fast-API"}

@app.get("/metadata/")
async def get_metadata():
    return {
        "sample": "data"
        }

app.include_router(api_router)
app.mount("/ws", ws)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	logging.error(f"{request}: {exc_str}")
	content = {'status_code': 10422, 'message': exc_str, 'data': None}
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

# if __name__ == '__main__':
#     uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
#     print("running")




