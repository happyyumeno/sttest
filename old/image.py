
import streamlit as st
from PIL import Image



st.title('AI for Images!📷')
st.markdown('**画像**向けのAIデモページです！')
input_file = st.file_uploader(label='Upload Image File!',type=['png','jpg'])

clm1, clm2 = st.columns([1, 1.5])
with clm1:
    if input_file is not None:
        img = Image.open(input_file)
        st.image(img)

with clm2:
    img = Image.open('ccc.JPG')
    st.image(img)
