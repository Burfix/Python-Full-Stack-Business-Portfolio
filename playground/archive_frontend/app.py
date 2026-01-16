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

        col1, col2, col3 = st.columns(3)
        col1.metric("Cheapest Total", f"R{data.get('total_cheapest', 'N/A')}")
        col2.metric("Most Expensive Total", f"R{data.get('total_most_expensive', 'N/A')}")
        col3.metric("Potential Savings", f"R{data.get('total_savings', 'N/A')}")

        st.subheader("Savings by Item")
        st.json(data["savings_by_item"])

        st.subheader("Supplier Scoreboard")
        st.json(data["supplier_scoreboard"])
    else:
        st.error(response.json().get("detail", "Something went wrong"))

