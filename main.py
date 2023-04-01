from fastapi import FastAPI, Depends

from pydantic import BaseModel

import database, models, schema
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/users')
def users(request: schema.Users, db: Session = Depends(get_db)):
    new_user = models.User()
    return {"something":"sk"}

@app.get('/products')
def home(db: Session = Depends(get_db)):
    product = db.query(models.Product).all()
    return product

@app.get('/products/{id}')
def home(id,db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    return product

@app.post('/post-item')
def post_item(request: schema.Products, db: Session = Depends(get_db)):
    new_product = models.Product(pname =request.pname, price = request.price, quantity = request.quantity )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product