from pydantic import BaseModel

class Products(BaseModel):
    id: int
    pname: str
    price: float
    quantity: int

class Users(BaseModel):
    id: int
    name: str
    fname: str
    pno: str
    addr:str

class ldc(BaseModel):
    pid: int
    like: int
    dislike: int
    comment: str