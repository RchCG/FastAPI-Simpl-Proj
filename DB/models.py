import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, UUID, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4())
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    company = Column(String, nullable=False)
    join_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    job_title = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
