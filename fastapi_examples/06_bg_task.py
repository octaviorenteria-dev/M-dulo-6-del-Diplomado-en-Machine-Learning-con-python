from fastapi import FastAPI
from pydantic import BaseModel
import time
import asyncio
import numpy as np

app = FastAPI()

class Point(BaseModel):
    timestamp:int
    value:float

async def server_loop():
    
    while True:
        timestamp = int(time.time())
        value = np.random.rand()
        point = Point(timestamp=timestamp, value=value)        
        await app.queue.put(point)
        await asyncio.sleep(1)

@app.on_event("startup")
def startup_event():    
    app.queue = asyncio.Queue()
    app.task = asyncio.create_task(server_loop())

@app.on_event("shutdown")
def shutdown_event():
    app.task.cancel()

@app.get("/get/")
async def get_item():

    if app.queue.qsize() == 0:
        return {'queue': 'empty'}
    items = []
    while app.queue.qsize() > 0:
        items.append(await app.queue.get())

    return items