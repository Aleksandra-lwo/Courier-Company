from sqlalchemy.orm import Session
from . import models, schemas
import base64


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session):
    return db.query(models.User).all()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = base64.b64encode(user.password.encode("utf-8")).__str__()
    db_user = models.User(
        email=user.email,
        hashed_password=fake_hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def change_user_membership(db: Session, user_id: int, membership: models.Membership):
    db.query(models.User).filter(models.User.id == user_id).update({"membership": membership})
    db.commit()
    return get_user(db, user_id)

