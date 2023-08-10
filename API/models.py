from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    job_title: str
    gender: str
    salary: int


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = None
    company: str | None = None
    job_title: str | None = None
    gender: str | None = None
    salary: int | None = None


class UserDeleteResponse(BaseModel):
    status: str = "USER_DELETED"


class UserCreatedResponse(BaseModel):
    status: str = "USER_CREATED"


class UserUpdateResponse(BaseModel):
    status: str = "USER_UPDATED"
