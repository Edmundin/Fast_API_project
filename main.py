# main.py

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    num1: int
    num2: int

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    item_dict.update({'sum': item_dict['num1'] + item_dict['num2']})
    return item_dict