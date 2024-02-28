from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base


# model for the DB
class Soldier(Base):
    __tablename__ = "soldiers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
