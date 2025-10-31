#!/usr/bin/env python
# coding: utf-8

import requests
import streamlit as st
from PIL import Image, ImageDraw
from streamlit_image_coordinates import streamlit_image_coordinates

import base64
from io import BytesIO
from PIL import Image
import numpy as np

def add_point():
    raw_value = st.session_state["pil"]
    value = raw_value["x"], raw_value["y"]

    st.session_state["points"].append(value+(st.session_state['label'],))

def get_ellipse_coords(point, w=5, h=5):
    x,y,l = point
    return [(x-w, y-h), (x+w, y+h)],"blue" if l else "red"


img = Image.new("RGB", (640,480))

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    image_stream = BytesIO(bytes_data)
    img = Image.open(image_stream)
    img = img.resize((640, 480))
    st.session_state['seg'] = img.copy()

if 'points' not in st.session_state:
    st.session_state['points'] = []
if 'label' not in st.session_state:
    st.session_state['label'] = 1
if 'seg' not in st.session_state:
    st.session_state['seg'] = img.copy()

clean, process, positives, negatives = st.columns(4)

if positives.button("Positive", key=2, use_container_width=True):
    st.session_state['label'] = 1
if negatives.button("Negative", key=3, use_container_width=True):
    st.session_state['label'] = 0
if clean.button("Clean", key=0, use_container_width=True):
    st.session_state['points'] = []
    st.session_state['seg'] = img.copy()
if process.button("Process", key=1, use_container_width=True):
    im_file = BytesIO()
    img.save(im_file, format="JPEG")

    im_bytes = im_file.getvalue()
    im_b64_bytes = base64.b64encode(im_bytes)
    im_b64_string = im_b64_bytes.decode('utf-8')


    url = 'http://127.0.0.1:8080/image'
    payload = {'imgb64': im_b64_string, 'points':[{'x':x,'y':y, 'l':l} for x,y,l in st.session_state['points']]}
    x = requests.post(url, json = payload)
    result = x.json()
    
    st.session_state['seg']  = Image.open(BytesIO(base64.b64decode(result['segmentation'])))


blend = Image.blend(img, st.session_state['seg'], alpha=0.5)

draw = ImageDraw.Draw(blend)

for point in st.session_state["points"]:
    coords,color = get_ellipse_coords(point)
    draw.ellipse(coords, fill=color)

def convert_for_download(img):
    img_array = np.asarray(img)
    msk_array = np.asarray(st.session_state['seg'])

    final = np.dstack([img_array,msk_array[:,:,0]])

    buffered = BytesIO()
    Image.fromarray(final).save(buffered, format="PNG")
    return buffered

value = streamlit_image_coordinates(blend, key="pil", on_click=add_point)

fimg = convert_for_download(img)

st.download_button(
    label="Download PNG",
    data=fimg,
    file_name="data.png",
    mime="image/png",
    icon=":material/download:",
)