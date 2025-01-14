from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    note = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    temporary_key = Column(String, unique=True, nullable=False)
    is_confirmed = Column(Boolean, nullable=False, default=False)
