import asyncio
from fastapi import FastAPI
from time import sleep

app = FastAPI()
shared_resource_lock = asyncio.Lock()
shared_data = {"counter": 0}

@app.get("/increment")
def increment_counter():
    shared_data["counter"] += 1
    sleep(0.1)        
    current_value = shared_data["counter"]
    shared_data["counter"] = 0
    return {"c": f"{current_value}"}

@app.get("/increment1")
async def increment_counter_async():
    async with shared_resource_lock:
        shared_data["counter"] += 1    
        #asyncio.sleep(0.1)
        sleep(0.1)
        current_value = shared_data["counter"]
        shared_data["counter"] = 0
    return {"c": f"{current_value}"}