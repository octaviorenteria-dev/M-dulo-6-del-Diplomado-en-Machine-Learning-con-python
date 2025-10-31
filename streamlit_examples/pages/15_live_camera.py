import streamlit as st
from PIL import Image
from io import BytesIO
from camera_input_live import camera_input_live
from ultralytics import YOLO

@st.cache_resource
def load_model():
    model = YOLO("yolo11n.pt")
    model = model.to('cuda')
    return model

model = load_model()

image = camera_input_live()

if image:
    
    image_bytes = image.getvalue()

    image_stream = BytesIO(image_bytes)
    image = Image.open(image_stream)
    results = model(image)
    image_with_boxes = results[0].plot()
    st.image(image_with_boxes, channels="BGR")
