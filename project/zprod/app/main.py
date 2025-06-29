# zprod/app/main.py
from fastapi import FastAPI
from app.routers.zprod_router import router

app = FastAPI()
app.include_router(router)