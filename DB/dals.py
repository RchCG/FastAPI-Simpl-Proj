from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import select, update, and_
from sqlalchemy.ext.asyncio import AsyncSession

from DB.models import User


class UserDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, name: str, email: EmailStr, age: int, company: str, job_title: str, gender: str,
                          salary: int) -> User:
        created_user = User(name=name, email=email, age=age, company=company, job_title=job_title, gender=gender,
                            salary=salary)
        self.db_session.add(created_user)
        await self.db_session.flush()
        return created_user

    # Get users
    async def get_users(self, salary_gt: int, salary_lt: int, name: str, ordering: str, offset: int, limit: int):
        query = select(User).where(User.is_active == True)
        if salary_gt is not None:
            query = query.where(User.salary > salary_gt)

        if salary_lt is not None:
            query = query.where(User.salary < salary_lt)

        if name is not None:
            query = query.filter(User.name.ilike(f"%{name}%"))

        query = query.order_by(ordering).offset(offset).limit(limit)
        result = await self.db_session.execute(query)
        users = result.scalars().all()
        return users

    # Get certain user
    async def read_user_by_id(self, target_user_id: UUID):
        query = select(User).where(and_(User.id == target_user_id, User.is_active == True))
        result = await self.db_session.execute(query)
        user = result.scalars().one()
        return user

    # Update certain user
    async def update_user_by_id(self, target_user_id: UUID, **kwargs):
        query = update(User).where(and_(User.id == target_user_id, User.is_active == True)).values(kwargs)
        await self.db_session.execute(query)

    # Delete certain user
    async def delete_user_by_id(self, target_user_id: UUID):
        query = update(User).where(and_(User.id == target_user_id, User.is_active == True)).values(
            is_active=False)
        await self.db_session.execute(query)
