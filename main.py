import streamlit as st
from PIL import Image
import rembg as bg

st.set_page_config(page_title="test run")
st.title("Lets Remove Backgrounds")
img = st.file_uploader("upload file here")

if img: 
    with open(img.name,"wb") as f:
        f.write(img.getbuffer())

    st.image(img)
    img2 = Image.open(img.name)
    extr = bg.remove(img2)
    st.image(extr)


