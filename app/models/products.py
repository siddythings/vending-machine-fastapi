from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base, engine

# SQL Model for Product


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    seller_id = Column(Integer, ForeignKey("users.id"))

    # Relationship with the seller
    seller = relationship("User", back_populates="products")


Base.metadata.create_all(engine)
