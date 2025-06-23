# users/app/main.py
from fastapi import FastAPI
from app.routers.users_router import router as users_router

app = FastAPI()
app.include_router(users_router)