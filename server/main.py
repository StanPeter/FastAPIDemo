from typing import Union, Annotated
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allow CORS origin
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# model for pydantic
# class Soldier(BaseModel):
#     name: str
#     email: str
# is_offer: Union[bool, None] = None


# SOLDIERS: list[Item] = [
#     {"name": "Book 1", "price": 45.69, "is_offer": True},
#     {"name": "Book 2", "price": 35.69},
# ]


# make sure db is opened only when processing a request, then close it
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)


@app.post("/soldier", response_model=schemas.SoldierSchema)
async def create_soldier(soldier: schemas.SoldierBaseSchema, db: db_dependency):
    print("HEREEEEEE")

    # found_soldier = db.query(models.Soldier).filter(
    #     models.Soldier.email == soldier.name or models.Soldier.name == soldier.name
    # )

    # if found_soldier:
    #     return HTTPException(status_code=409, detail="Soldier already exists")

    new_soldier = models.Soldier(**soldier.model_dump())

    db.add(new_soldier)
    db.commit()
    db.refresh(new_soldier)
    return new_soldier


@app.get("/soldier", response_model=list[schemas.SoldierSchema])
async def get_soldiers(db: db_dependency):
    return db.query(models.Soldier).all()


@app.get("/soldier/{soldier_id}", response_model=schemas.SoldierSchema)
async def get_soldier(soldier_id: int, db: db_dependency):
    return db.query(models.Soldier).filter(models.Soldier.id == soldier_id).first()


@app.put("/soldier/{soldier_id}", response_model=schemas.SoldierSchema)
async def modify_soldier(
    soldier_id: int, db: db_dependency, soldier: schemas.SoldierBaseSchema
):
    db.merge


# def get_soldier(db: Session, soldier_id: int):
#     return db.query(models.Soldier).filter(models.Soldier.id == soldier_id).first()


# def create_soldier(db: Session, user: schemas.SoldierCreate):
#     db_soldier = models.Soldier(email=user.email)
#     db.add(db_soldier)
#     db.commit()
#     db.refresh(db_soldier)
#     return db_soldier


# @app.get("/items")
# def get_items():
#     return SOLDIERS


# @app.get("/items/{item_id}")
# def get_item(item_id: int, q: Union[str, None] = None):
#     return MOCK_DATA_ITEMS[0]


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name}
