from DB.models import User
from sqlalchemy.orm import Session


def salary_gt(gt: int, db: Session):
    query = db.query(User).where(User.salary > gt).all()
    return query


def salary_lt(lt: int, db: Session):
    query = db.query(User).where(User.salary < lt).all()
    return query


def search_by_name(name: str, db: Session):
    query = db.query(User).where(User.name == name).all()

