# streamlit_app.py
import streamlit as st

c = st.number_input("Enter °C:")
f = (c * 9/5) + 32
st.write(f"{f:.2f} °F")