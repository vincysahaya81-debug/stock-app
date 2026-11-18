import streamlit as st
inventory = ["Rice - 10 Kg", "Sugar - 5 Kg", "Oil - 2 Litre", "Dal - 3 Kg"]

st.title("Stock App - Inventory List")
st.write("Unga Stock List Inga Irukku Ma!")

for item in inventory:
    st.write(item)
