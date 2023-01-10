import datetime

from .database import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime
import enum


class Membership(enum.Enum):
    CUSTOMER = "CUSTOMER"
    ADMIN = "ADMIN"
    COURIER = "COURIER"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    membership = Column(Enum(Membership), nullable=False, default=Membership.CUSTOMER.name)
    joined_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())