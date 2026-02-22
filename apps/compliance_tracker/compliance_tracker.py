import os
import pandas as pd
import json
from datetime import datetime, timedelta
import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Compliance Tracker | ForgeStack Africa",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DATA STORAGE ---
# Use /tmp for Streamlit Cloud (ephemeral) - this works for both local and cloud
DATA_DIR = "/tmp/compliance_data"
os.makedirs(DATA_DIR, exist_ok=True)

STORES_FILE = os.path.join(DATA_DIR, "stores.json")
COMPLIANCE_FILE = os.path.join(DATA_DIR, "compliance_records.json")

# --- SAMPLE DATA FOR DEMO ---
SAMPLE_STORES = [
    {"id": 1, "name": "Cape Town CBD Branch", "region": "Western Cape", "manager": "Thabo Mokoena"},
    {"id": 2, "name": "Johannesburg Sandton", "region": "Gauteng", "manager": "Sarah Naidoo"},
    {"id": 3, "name": "Durban North", "region": "KwaZulu-Natal", "manager": "Rajesh Govender"},
    {"id": 4, "name": "Port Elizabeth", "region": "Eastern Cape", "manager": "Linda Mxenge"},
]

SAMPLE_COMPLIANCE = [
    {
        "id": 1,
        "store_id": 1,
        "category": "Fire Safety Certificate",
        "status": "Compliant",
        "last_audit": "2025-11-15",
        "next_due": "2026-11-15",
        "reviewer": "Inspector Johnson",
        "notes": "All extinguishers serviced"
    },
    {
        "id": 2,
        "store_id": 1,
        "category": "Liquor License",
        "status": "Action Required",
        "last_audit": "2024-06-20",
        "next_due": "2025-06-20",
        "reviewer": "SARS Licensing",
        "notes": "Renewal application pending"
    },
    {
        "id": 3,
        "store_id": 2,
        "category": "Health & Safety",
        "status": "Compliant",
        "last_audit": "2025-01-10",
        "next_due": "2026-01-10",
        "reviewer": "Dept of Labour",
        "notes": "Full compliance achieved"
    },
]

def load_data():
    """Load data from JSON or initialize with sample data"""
    if not os.path.exists(STORES_FILE):
        with open(STORES_FILE, 'w') as f:
            json.dump(SAMPLE_STORES, f)
    if not os.path.exists(COMPLIANCE_FILE):
        with open(COMPLIANCE_FILE, 'w') as f:
            json.dump(SAMPLE_COMPLIANCE, f)
    
    with open(STORES_FILE, 'r') as f:
        stores = json.load(f)
    with open(COM
