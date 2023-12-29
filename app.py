# app.py
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME"),
    openapi_url="/api/v1/openapi.json",
    redoc_url=None,
    docs_url="/api/v1/docs"
)

custom_tag = {"Fast API"}