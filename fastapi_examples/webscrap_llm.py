from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
from typing import List

import logging
import html2text
import requests
import asyncio
import ollama


app = FastAPI()
ollama_client =  ollama.AsyncClient(host="http://localhost:11434")

logging.basicConfig(

    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",

)
logger = logging.getLogger(__name__)

class Quote(BaseModel):
    name: str
    text: str

class Quotes(BaseModel):
    quotes: List[Quote]

async def server_loop():
    h = html2text.HTML2Text()
    prompt = '''
    The following context contains a list of quotes. Extract the quotes in JSON format.
    Each object in the list has the following properties:
    Key "text": the text of the quote.
    Key "name": the name of the author of the quote.
    Return this list as a JSON object with the key "quotes".
    CONTEXT:
    '''
    while True:
        page = await app.queue_page.get()
        r = requests.get(f'https://quotes.toscrape.com/page/{page}/')
        text = h.handle(r.text)
        
        logger.info(text) 

        response = await ollama_client.generate(model='gemma3:12b', prompt=prompt+text, format=Quotes.model_json_schema(), stream=False)

        data = Quotes.model_validate_json(response['response'])

        logger.info(data)    
        await app.queue_results.put(data)

@app.get("/")
async def root():
    return {"message": "This page scraps data from the page https://quotes.toscrape.com"}

@app.on_event("startup")
def startup_event():    
    app.queue_page = asyncio.Queue()
    app.queue_results = asyncio.Queue()
    app.task = asyncio.create_task(server_loop())

@app.get("/put/{page_id}")
async def put_item(page_id:int):
    await app.queue_page.put(page_id)
    return {"page_id": page_id}

@app.get("/get")
async def get_item():
    
    if app.queue_results.qsize() == 0:
        return {'queue': 'empty'}

    items = []
    while app.queue_results.qsize() > 0:
        items.append(await app.queue_results.get())

    return items