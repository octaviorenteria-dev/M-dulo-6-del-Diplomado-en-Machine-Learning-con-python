from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    nombre: str
    edad: int
    estado: str | None = None

@app.on_event("startup")
def startup_event():
    app.data = list()

@app.get("/get/")
def get_item():
    if len(app.data) == 0:
        return {"data":"empty"}
    return app.data

@app.get("/delete/")
def get_item():
    app.data = list()
    return {"data":"empty"}
    
@app.post("/put/")
def put_item(item: Item):
    app.data.append(item)
    return item