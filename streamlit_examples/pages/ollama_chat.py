import ollama
import streamlit as st

client = ollama.Client(host='http://127.0.0.1:11434')
models = [m.model for m in client.list().models]

def generate(prompt, model='gemma3:12b'):
    stream = client.generate(model=model, prompt=prompt, stream=True)
    for chunk in stream:
        yield chunk['response']


st.write_stream(generate(prompt='tell me a joke'))