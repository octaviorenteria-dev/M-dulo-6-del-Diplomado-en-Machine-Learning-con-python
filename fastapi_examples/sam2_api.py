from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import logging

from PIL import Image
from io import BytesIO
import base64

import numpy as np
import asyncio
import torch
from transformers import Sam2Processor, Sam2Model, infer_device

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",

    datefmt="%Y-%m-%d %H:%M:%S",

)


# Create a logger instance

logger = logging.getLogger(__name__)

app = FastAPI()

class Point(BaseModel):
    x:int
    y:int
    l:int

class Item(BaseModel):
    imgb64: str
    points: List[Point]=None

async def server_loop(in_queue, out_queue):
    device = infer_device()
    model = Sam2Model.from_pretrained("facebook/sam2.1-hiera-large").to(device)
    processor = Sam2Processor.from_pretrained("facebook/sam2.1-hiera-large")

    while True:
        item = await in_queue.get()

        input_points = [[[[i.x,i.y] for i in item.points]]]
        input_labels = [[[i.l for i in item.points]]]
        logging.info(input_points)
        logging.info(input_labels)
        
        

        img = Image.open(BytesIO(base64.b64decode(item.imgb64)))
        if len(input_points[0][0]) > 0:
            inputs = processor(images=img, input_points=input_points, input_labels=input_labels, return_tensors="pt").to(model.device)
        else:
            inputs = processor(images=img, points_per_batch=64, return_tensors="pt").to(model.device)
        

        with torch.no_grad():
            outputs = model(**inputs)
        masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])[0]
        masks = masks.numpy()
        masks = masks[0].astype(np.uint8)
        masks = np.transpose(masks,(1,2,0))
        

        
        xx = np.dstack([masks[:,:,1],masks[:,:,1],masks[:,:,1]]) * 255 

        img = Image.fromarray(xx)


        await out_queue.put(img)

@app.on_event("startup")
def startup_event():
    
    in_queue = asyncio.Queue()    
    out_queue = asyncio.Queue()
    
    app.in_queue = in_queue
    app.out_queue = out_queue

    asyncio.create_task(server_loop(in_queue, out_queue))

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/image")
async def process(item: Item):
    
    await app.in_queue.put(item)


    result = await app.out_queue.get()

    im_file = BytesIO()
    result.save(im_file, format="JPEG")

    im_bytes = im_file.getvalue()
    im_b64_bytes = base64.b64encode(im_bytes)
    im_b64_string = im_b64_bytes.decode('utf-8')

    logging.info(result)
    return {"segmentation": im_b64_string}