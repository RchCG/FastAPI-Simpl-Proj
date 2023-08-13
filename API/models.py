from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(gt=0, lt=130)
    company: str
    job_title: str
    gender: str
    salary: int = Field(gt=0)


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, examples=["Daniil"])
    email: EmailStr | None = None
    age: int | None = Field(default=None, gt=0, lt=130, examples=['0<age<130'])
    company: str | None = Field(default=None, examples=["VeryCoolCompany"])
    job_title: str | None = Field(default=None, examples=["VeryCoolJob"])
    gender: str | None = Field(default=None, examples=["Male or Female"])
    salary: int | None = Field(default=None, gt=0, examples=['Greater than 0'])

    class config:
        orm_mode = True


class UserDeleteResponse(BaseModel):
    status: str = "USER_DELETED"


class UserCreatedResponse(BaseModel):
    status: str = "USER_CREATED"


class UserUpdateResponse(BaseModel):
    status: str = "USER_UPDATED"
