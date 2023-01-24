from fastapi import FastAPI
from app.api import api_router

appFast = FastAPI(
    title='Belanjaku POS - Auth JWT Token',
    version='1.0.0'
)

appFast.include_router(api_router)