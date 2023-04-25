import streamlit as st

st.title("Image Editor")

filters = ["Contour","Detail","Blur","Sharpen"]

with st.sidebar:
  filters_selected = st.multiselect("Elige",filters)
  
fichero = st.file_uploader("Elige tu imagen", type=['png','jpg'])

col1,col2 = st.columns(2)

with col1:
  st.header("Original")
  
with col2:
  st.header("Edited")
