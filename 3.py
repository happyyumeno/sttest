
import streamlit as st
import os


basename = os.path.basename(__file__)
basename = os.path.splitext(basename)[0]
basename1,basename2,basename3 =basename.split('_')

st.title(basename1)
st.title(basename3)
