from sqlalchemy import Column, String, Integer

from .database import Base


class Person(Base):
  __tablename__ = 'persons'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
