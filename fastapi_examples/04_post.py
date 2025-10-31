from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    nombre: str
    edad: int
    estado: str | None = None

app = FastAPI()

@app.post("/items/")
def create_item(item: Item):
    return item