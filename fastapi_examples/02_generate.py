from fastapi import FastAPI
import ollama
app = FastAPI() #1
ollama_client = ollama.Client(host="http://localhost:11434") #2
@app.get("/")
def root_controller():
    return {"status": "healthy"}

@app.get("/generate") #3
def generate_controller():
    prompt = "Tell me a joke"
    response = ollama_client.generate(model='gemma3:12b', prompt=prompt, stream=False) #4
    return {"statement": response['response']} #5

@app.get("/status")
def status_controller():
    return {'status':'ok'}