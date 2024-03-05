from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base, engine

# SQL Model for User


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    role = Column(String)

    # Relationship with products
    products = relationship("Product", back_populates="seller")


Base.metadata.create_all(engine)
