import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, UUID, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    is_active = Column(Boolean(), default=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    company = Column(String, nullable=False)
    join_date = Column(DateTime, default=datetime.utcnow)
    job_title = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
