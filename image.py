
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt



st.title('AI for Images!ð·')
st.markdown('**ç»å**åãã®AIãã¢ãã¼ã¸ã§ãï¼')
input_file = st.file_uploader(label='Upload Image File!',type=['png','jpg'])

clm1, clm2 = st.columns([1, 1.5])
with clm1:
    if input_file is not None:
        img = Image.open(input_file)
        st.image(img)
