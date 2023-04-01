from database import *
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    pname = Column(String, unique=True)
    price = Column(String)
    quantity = Column(String)

    # items = relationship("Item", back_populates="owner")

class User(Base):
    __tablename__ = "user"

    id= Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    fname = Column(String)
    pno = Column(Integer)
    addr = Column(String)
