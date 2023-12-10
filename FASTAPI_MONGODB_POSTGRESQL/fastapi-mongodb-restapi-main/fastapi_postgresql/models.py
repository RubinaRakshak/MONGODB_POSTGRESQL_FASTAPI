from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from .database import Base


class CreateJobRequest(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone = password = Column(String, nullable=False)
