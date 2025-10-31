#!/usr/bin/env python
# coding: utf-8
import ollama
import time 
import streamlit as st
import base64
import copy

st.title("Simple LLM chat")

client = ollama.Client(host='http://127.0.0.1:11434')
clist = client.list()
models = sorted([m.model for m in clist.models ])


if 'text' not in st.session_state:
    st.session_state['text']=""
if 'context' not in st.session_state:
    st.session_state['context']=None

if 'image' not in st.session_state:
    st.session_state['image']=None

if 'b64_image' not in st.session_state:
    st.session_state['b64_image']=None

option = st.selectbox(
    "Select model",
    models,
)


prompt = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)




if prompt and prompt["files"]:
    data_bytes = prompt["files"][0].read()
    st.session_state['b64_image'] = base64.b64encode(data_bytes).decode('utf-8')
    st.session_state['image'] = prompt["files"][0]

if st.session_state['image'] is not None:
    st.image(st.session_state['image'],width=300)

if prompt and prompt.text:
    placeholder = st.empty()

    if st.session_state['b64_image'] is None:
        stream = client.generate(model=option, prompt=prompt.text, stream=True, context=st.session_state['context'])
    else:
        stream = client.generate(model=option, prompt=prompt.text, images=[st.session_state['b64_image']], stream=True, context=st.session_state['context'])
    #log_text=''
    

    for chunk in stream:
        st.session_state['text'] += chunk['response']
        placeholder.write(f"{st.session_state['text']}")
    st.session_state['text']+='\n\n'
    st.session_state['context']=copy.copy(chunk['context'])

