# auth/app/routers/auth_router.py
from fastapi import APIRouter
from app.models.user import UserCreate, UserResponse

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    # Пример логики регистрации
    return {
        "id": 1,
        "username": user.username
    }