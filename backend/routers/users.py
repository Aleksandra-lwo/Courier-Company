from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    tags=["users"],
    prefix="/api/v1/users"
)


class Authentication(BaseModel):
    login: str
    password: str

@router.get("/")
async def read_users():
    return []


@router.get("/{user_id}")
async def read_user_by_id(user_id: int):
    return {
        "user_id": user_id
    }


@router.post("/sign-in")
async def sign_in(credentials: Authentication):
    return {
        "login": credentials.login
    }


@router.post("/sign-up")
async def sign_up(credentials: Authentication):
    return {
        "login": credentials.login
    }

