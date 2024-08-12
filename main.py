from fastapi import FastAPI, Depends, Header, status, HTTPException

from pydantic import BaseModel

import database, models, schema
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_authorization_header(authorization: str = Header(None)):
    if authorization != "siu":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/project-x')
def secure_endpoint(authorization: str = Depends(verify_authorization_header)):
    # If authorization header is correct
    return {"message": "Cristiano Ronaldo siuuuuuuuuuu"}

@app.post('/users')
def users(request: schema.Users, db: Session = Depends(get_db)):
    new_user = models.User(name = request.name, fname = request.fname, pno = request.pno, addr = request.addr)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

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

@app.post('like-dislike-comment')
def likeDislikeComment(id, request: schema.ldc, db: Session = Depends(get_db)):
    pId = db.query(models.Product).filter(models.Product.id==id).first()
    return pId
