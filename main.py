from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


MOCK_DATA_ITEMS: list[Item] = [
    {"name": "Book 1", "price": 45.69, "is_offer": True},
    {"name": "Book 2", "price": 35.69},
]


@app.get("/items")
def get_items():
    return MOCK_DATA_ITEMS


@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
    return MOCK_DATA_ITEMS[0]


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name}
