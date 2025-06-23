# users/app/models/user.py
from pydantic import BaseModel

class UserInDB(BaseModel):
    user_id: int
    name: str
    email: str | None = None

class UserCreate(BaseModel):
    name: str
    email: str