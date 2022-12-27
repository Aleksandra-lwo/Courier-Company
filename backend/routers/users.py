from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sql import schemas, crud, main, models
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["users"],
    prefix="/api/v1/users"
)


class Authentication(BaseModel):
    email: str
    password: str


class Parameters(BaseModel):
    membership: models.Membership


@router.get("/", response_model=list[schemas.User])
async def read_users(db: Session = Depends(main.get_db)):
    users = crud.get_users(db)
    return users


@router.get("/{user_id}", response_model=schemas.User)
async def read_user_by_id(user_id: int, db: Session = Depends(main.get_db)):
    user = crud.get_user(db, user_id)
    return user


@router.patch("/{user_id}", response_model=schemas.User)
async def change_membership(user_id: int, parameters: Parameters, db: Session = Depends(main.get_db)):
    user = crud.change_user_membership(db, user_id, parameters.membership)
    return user


@router.post("/sign-in")
async def sign_in(credentials: Authentication):
    return {
        "login": credentials.login
    }


@router.post("/sign-up")
async def sign_up(user: schemas.UserCreate, db: Session = Depends(main.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)



