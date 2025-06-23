# auth/app/main.py
from fastapi import FastAPI
from app.routers.auth_router import router as auth_router

app = FastAPI()
app.include_router(auth_router)