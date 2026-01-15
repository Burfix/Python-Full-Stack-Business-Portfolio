import streamlit as st
import requests

st.set_page_config(page_title="Supplier Price Dashboard", layout="centered")

st.title("Supplier Price Intelligence")
st.write("Upload an invoice CSV to find the cheapest supplier per item.")

API_URL = "http://127.0.0.1:8001/upload"

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    files = {"file": uploaded_file}
    response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        data = response.json()

        st.subheader("Cheapest Suppliers")
        st.json(data["cheapest"])

        st.metric("Total (1 of each item)", f"R{data['total']}")
    else:
        st.error(response.json().get("detail", "Something went wrong"))
