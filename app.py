import streamlit as st
from inventory import inventory

st.title("Stock App - Inventory List")
st.write("Unga Stock List Inga Irukku Ma!")

for item in inventory:
    st.write(item)
