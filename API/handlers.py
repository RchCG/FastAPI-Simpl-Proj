from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.User.crud import register_new_user, update_user_data, delete_user_data, read_users, read_user_by_id
from fastapi import APIRouter, Depends, HTTPException, Query
from API.models import UserCreatedResponse, UserUpdateResponse, UserUpdate, UserCreate, UserDeleteResponse
from DB.session import get_db

users_router = APIRouter(prefix="/api/v1/users", tags=["UsersCRUD"])


@users_router.post("/", tags=['UsersCRUD'], summary="Создать нового пользователя.",
                   status_code=201, response_model=UserCreatedResponse)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    **name: str**\n
    **email: EmailStr**\n
    **age: int, Greater than 0 and lower than 130**\n
    **company: str**\n
    **job_title: str**\n
    **gender: str, Male or Female**\n
    **salary: int, Greater than 0**\n
    """
    return await register_new_user(body=body, db=db)


@users_router.get("/api/v1/users/", summary="Получить отфильтрованных доступных пользователей из БД")
async def get_users(
        salary_gt: int = Query(None, description="Заработная плата работника больше чем"),
        salary_lt: int = Query(None, description="Заработная плата работника меньше чем"),
        name: str = Query(None, description="Поиск по имени пользователя"),
        limit: int = Query(10, description="Количество объектов в ответе"),
        offset: int = Query(0, description="С какого по счёту объекта наччать выборку"),
        ordering: str = Query("name", description="Колонка для сортировки и порядок сортировки(без - и с ним)"),
        db: AsyncSession = Depends(get_db),
):
    result = await read_users(salary_gt=salary_gt, salary_lt=salary_lt, name=name, ordering=ordering, offset=offset,
                              limit=limit, db=db)
    if result is None:
        raise HTTPException(status_code=404, detail="Something went wrong")

    count = len(result)
    return {"COUNT OF ITEMS": count, "YOUR RESULT": result}


@users_router.get("/{target_user_id}", summary="Получить данные пользователя по ID")
async def get_user_by_id(target_user_id: UUID, db: AsyncSession = Depends(get_db)):
    user = await read_user_by_id(target_user_id=target_user_id, db=db)
    return user


@users_router.patch("/{target_user_id}", summary="Обновить данные пользователя по ID.",
                    response_model=UserUpdateResponse)
async def update_user_details(body: UserUpdate, target_user_id: UUID, db: AsyncSession = Depends(get_db)):
    update_user_params = body.model_dump(exclude_none=True)
    user = await update_user_data(body=update_user_params, target_user_id=target_user_id, db=db)
    return UserUpdateResponse


@users_router.delete("/{target_user_id}", summary="Удалить пользователя по ID.",
                     response_model=UserDeleteResponse)
async def delete_user(target_user_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await delete_user_data(target_user_id=target_user_id, db=db)
    if result is None:
        raise HTTPException(status_code=404, detail=f"User with id {target_user_id} not found.")
    return UserDeleteResponse
