from pydantic import BaseModel
from pydantic.networks import EmailStr
import datetime


class UserResponse(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime.datetime
    job_title: str
    gender: str
    salary: int