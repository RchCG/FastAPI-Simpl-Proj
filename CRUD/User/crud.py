from uuid import UUID

from API.models import UserCreate
from DB.dals import UserDAL


async def register_new_user(body: UserCreate, db):
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(name=body.name, age=body.age, email=body.email, company=body.company,
                                              job_title=body.job_title, gender=body.gender, salary=body.salary)
            return user


async def read_users(salary_gt: int, salary_lt: int, name: str, ordering: str, offset: int, limit: int, db):
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            users = await user_dal.get_users(salary_gt=salary_gt, salary_lt=salary_lt, name=name, ordering=ordering,
                                             offset=offset, limit=limit)

            return users


async def read_user_by_id(target_user_id: UUID, db):
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.read_user_by_id(target_user_id=target_user_id)
            return user


async def update_user_data(body: dict, target_user_id: UUID, db):
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            updated_user = await user_dal.update_user_by_id(**body, target_user_id=target_user_id)
            return updated_user


async def delete_user_data(target_user_id: UUID, db):
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            deleted_user = await user_dal.delete_user_by_id(target_user_id=target_user_id)
            return deleted_user
