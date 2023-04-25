import streamlit as st

st.title("Image Editor")

with st.sidebar():
  filters = st.multiselect("Elige"["Contour","Detail","Blur","Sharpen"])
