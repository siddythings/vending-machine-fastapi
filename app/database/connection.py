from sqlalchemy.orm import sessionmaker
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
