from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}

@app.get("/range/")
def read_range(start, stop, step):
    numbers = list(range(int(start), int(stop), int(step)))
    return {'numbers': numbers}

@app.get("/range_valid/")
def read_range_valid(stop:int, start:int=0, step:int=1, reverse: str | None = None):
    numbers = list(range(int(start), int(stop), int(step)))
    stp = -1 if reverse is not None else 1
    return {'numbers': numbers[::stp]}

@app.get("/items_constr/{item_id}")
def read_item(item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)] ):
    return {"item_id": item_id}

@app.get("/range_constr/")
def read_range_constr(  stop:Annotated[int, Query(title="stop number", ge=1)],
                        start:Annotated[int, Query(title="start number", ge=0)]=0,
                        step:Annotated[int, Query(title="step number", ge=1)]=1,
                        reverse: str | None = None):
    numbers = list(range(int(start), int(stop), int(step)))
    stp = -1 if reverse is not None else 1
    return {'numbers': numbers[::stp]}