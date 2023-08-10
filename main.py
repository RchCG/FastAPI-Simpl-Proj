from fastapi import FastAPI, Depends, Query
from DB.models import User
from DB.session import get_db, Session
from routers.handlers import users_router

app = FastAPI(title="UsersFiltrationWithoutSQL")
app.include_router(users_router)


@app.get("/api/v1/users/", summary="Получить отфильтрованных доступных пользователей из БД", tags=["BD Manipulation"])
async def get_users(
        salary_gt: int = Query(None, description="Заработная плата работника больше чем"),
        salary_lt: int = Query(None, description="Заработная плата работника меньше чем"),
        name: str = Query(None, description="Поиск по имени пользователя"),
        limit: int = Query(10, description="Количество объектов в ответе"),
        offset: int = Query(0, description="С какого по счёту объекта наччать выборку"),
        ordering: str = Query("name", description="Колонка для сортировки и порядок сортировки(без - и с ним)"),
        db: Session = Depends(get_db),
):
    """**Получить список пользователей**"""
    query = db.query(User)

    if salary_gt is not None:
        query = query.filter(User.salary > salary_gt)

    if salary_lt is not None:
        query = query.filter(User.salary < salary_lt)

    if name is not None:
        query = query.filter(User.name.ilike(f"%{name}%"))

    query = query.order_by(ordering).offset(offset).limit(limit)
    users = query.all()
    count = len(users)
    return {"COUNT OF ITEMS": count, "YOUR RESULT": users}