from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model():
    model = pipeline("image-classification", model="microsoft/resnet-50", device="cuda")
    return model

st.title("Model loading and cache")
st.subheader("resnet-50")

model = load_model()

url = 'https://raw.githubusercontent.com/google-coral/test_data/master/cat_720p.jpg'

user_input = st.text_input("Enter image url:",value=url)
if user_input:
    url = user_input
    
st.image(url)
results = model(url)
for r in results:
    text = f":blue-badge[{r['label']}] :green-badge[{r['score']*100:.1f}%]"
    st.markdown(text)