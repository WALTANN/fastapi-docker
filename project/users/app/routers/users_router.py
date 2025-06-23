# users/app/routers/users_router.py
from fastapi import APIRouter
from app.models.user import UserInDB, UserCreate

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/users", response_model=UserInDB)
def create_user(user: UserCreate):
    # Пример создания пользователя
    return {
        "user_id": 101,
        "name": user.name,
        "email": user.email
    }