from database import *
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    pname = Column(String,)
    price = Column(String)
    quantity = Column(String)

    # items = relationship("Item", back_populates="owner")

class User(Base):
    __tablename__ = "user"

    id= Column(Integer, primary_key=True, index=True)
    name = Column(String,)
    fname = Column(String)
    pno = Column(String, unique=True)
    addr = Column(String)


#likedislkikecomment >>>>>>>>>>>> ldc
class Ldc(Base):
    __tablename__ = "ldc"

    id= Column(Integer, primary_key=True, index=True)
    pid = Column(Integer )
    like= Column(Integer)
    dislike = Column(Integer)
    comment = Column(String)
