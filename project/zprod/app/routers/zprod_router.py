# zprod/app/routers/zprod_router.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def ping():
    return {"message": "its my 3d service, i do it for my itmo practice project at 2nd course on robotics, lmao xD"}

@router.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Lapop (Laptop?)", "price": 100001010990},
        {"id": 2, "name": "iPhone 30 pro ultra max galaxy nerealka", "price": 5000000},
        {"id": 3, "name": "Practice-point", "point": 5},
        {"id": 4, "name": "T-shka", "price": 1345678213}
    ]