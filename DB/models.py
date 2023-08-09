import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, UUID, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String)
    email = Column(String, unique=True)
    age = Column(Integer)
    company = Column(String)
    join_date = Column(DateTime, default=datetime.utcnow)
    job_title = Column(String)
    gender = Column(String)
    salary = Column(Integer)