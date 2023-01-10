from pydantic import BaseModel
from . import models


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    membership: models.Membership
    joined_at: object

    class Config:
        orm_mode = True
