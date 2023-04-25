import streamlit as st

st.title("Image Editor")

filters = ["Contour","Detail","Blur","Sharpen"]

with st.sidebar:
  filters_selected = st.multiselect("Elige")
  
fichero = st.file_uploader("Elige tu imagen")
