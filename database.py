from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

connection_string = os.environ.get("CONNECTION_STRING")

engine = create_engine(connection_string, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

print(connection_string, " connection_string")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
