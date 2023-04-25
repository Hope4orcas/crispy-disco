import streamlit as st
from PIL import Image, ImageFilter

st.title("Image Editor")

filters = ["Contour","Detail","Blur","Sharpen"]

with st.sidebar:
  filters_selected = st.multiselect("Elige",filters)
  
fichero = st.file_uploader("Elige tu imagen", type=['png','jpg'])

if fichero:
  imagen_original = Image.open(fichero)
  imagen_editada = imagen_original

  col1,col2 = st.columns(2)

  with col1:
    st.header("Original")
    st.image(imagen_original)

  with col2:
    st.header("Edited")
    st.image(imagen_editada)
