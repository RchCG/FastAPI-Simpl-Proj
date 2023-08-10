from sqlalchemy.orm import Session

from API.models import UserBase, UserUpdate
from DB.models import User


def create_user(user: UserBase, db: Session):
    created_user = User(name=user.name, email=user.email, age=user.age, company=user.company, job_title=user.job_title,
                        gender=user.gender, salary=user.salary)
    db.add(created_user)
    db.commit()
    db.refresh(created_user)

    return created_user


def read_user_by_id(target_user_id: str, db: Session):
    query = db.query(User).where(User.id == target_user_id).first()

    return query


def update_user_by_id(user: UserUpdate, target_user_id: str, db: Session):
    new_user_details = db.query(User).where(User.id == target_user_id).first()
    update_dict = user.dict(exclude_unset=True)
    db.query(User).filter(User.id == target_user_id).update(update_dict)
    db.commit()
    db.refresh(new_user_details)

    return new_user_details


def delete_user_by_id(target_user_id: str, db: Session):
    deleted_user = db.query(User).where(User.id == target_user_id).first()
    db.delete(deleted_user)
    db.commit()

    return deleted_user
