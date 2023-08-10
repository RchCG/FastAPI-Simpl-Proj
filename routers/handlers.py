from API.crud import create_user, read_user_by_id, update_user_by_id, delete_user_by_id
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Body, HTTPException
from API.models import UserCreatedResponse, UserUpdateResponse, UserUpdate, UserCreate, UserDeleteResponse
from DB.session import get_db

users_router = APIRouter()


@users_router.post("/", response_model=UserCreatedResponse, tags=['UsersCRUD'], summary="Создать нового пользователя.")
async def register_new_user(user: UserCreate = Body(example={
    "name": "Victor",
    "email": "victor@gmail.com",
    "age": 22,
    "company": "Venture Structures",
    "job_title": "Manager",
    "gender": "Male",
    "salary": 100000
}), db: Session = Depends(get_db)):
    created_user = create_user(user=user, db=db)
    if created_user is None:
        raise HTTPException(status_code=404, detail="Невозможно создать пользователя с такими параметрами.")

    return UserCreatedResponse


@users_router.get("/{target_user_id}", tags=["UsersCRUD"], summary="Получить пользователя по ID.")
async def get_user_by_id(target_user_id: str, db: Session = Depends(get_db)):
    user = read_user_by_id(target_user_id=target_user_id, db=db)
    if user is None:
        raise HTTPException(status_code=404, detail="Не удалось найти пользователя с таким ID.")

    return user


@users_router.patch("/{target_user_id}", tags=["UsersCRUD"], summary="Обновить данные пользователя по ID.",
                    response_model=UserUpdateResponse)
async def update_user_details(user: UserUpdate, target_user_id: str, db: Session = Depends(get_db)):
    new_user_details = update_user_by_id(user=user, target_user_id=target_user_id, db=db)
    if new_user_details is None:
        raise HTTPException(status_code=404, detail="Не удалось внести изменения или внесены одинаковые данные.")

    return UserUpdateResponse


@users_router.delete("/{target_user_id}", tags=["UsersCRUD"], summary="Удалить пользователя по ID.",
                     response_model=UserDeleteResponse)
async def delete_user(target_user_id: str, db: Session = Depends(get_db)):
    deleted_user = delete_user_by_id(target_user_id=target_user_id, db=db)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="Не удалось удалить пользователя.")
    return deleted_user
