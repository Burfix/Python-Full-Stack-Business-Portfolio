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
    with open(COMPLIANCE_FILE, 'r') as f:
        compliance = json.load(f)
    
    return stores, compliance

def save_data(stores, compliance):
    """Save data to JSON"""
    with open(STORES_FILE, 'w') as f:
        json.dump(stores, f, indent=2)
    with open(COMPLIANCE_FILE, 'w') as f:
        json.dump(compliance, f, indent=2, default=str)

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 0.75rem;
        color: white;
    }
    .status-compliant { color: #10b981; font-weight: 600; }
    .status-pending { color: #f59e0b; font-weight: 600; }
    .status-action { color: #ef4444; font-weight: 600; }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 0.5rem;
        padding: 0.5rem 1.5rem;
        border: none;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    .footer {
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #e5e7eb;
        text-align: center;
        color: #9ca3af;
        font-size: 0.875rem;
    }
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1rem;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# --- MAIN APP ---
def main():
    # Header
    st.markdown('<p class="main-header">✅ Compliance Tracker</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Multi-location compliance management for South African retail operations</p>', unsafe_allow_html=True)
    
    # Load data
    stores, compliance = load_data()
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🔷 ForgeStack Africa")
        st.markdown("---")
        st.markdown("### 🏢 Quick Stats")
        
        total_stores = len(stores)
        total_records = len(compliance)
        compliant_count = len([c for c in compliance if c['status'] == 'Compliant'])
        action_required = len([c for c in compliance if c['status'] == 'Action Required'])
        
        st.metric("Total Stores", total_stores)
        st.metric("Compliance Records", total_records)
        st.metric("Compliant", f"{compliant_count}/{total_records}")
        
        if action_required > 0:
            st.error(f"⚠️ {action_required} Action Required")
        
        st.markdown("---")
        st.markdown("### 📍 Filter by Region")
        regions = list(set([s['region'] for s in stores]))
        selected_region = st.selectbox("Select Region", ["All"] + regions)
        
        st.markdown("---")
        st.markdown("**Made in Cape Town 🇿🇦**")
        st.markdown("*ForgeStack Africa*")
    
    # Main content tabs
    tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🏪 Stores", "➕ Add Record"])
    
    with tab1:
        # Metrics row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div style="background: #dbeafe; padding: 1rem; border-radius: 0.5rem; text-align: center;">
                <div style="font-size: 2rem; font-weight: bold; color: #1e40af;">{total_stores}</div>
                <div style="color: #3b82f6; font-size: 0.875rem;">Active Stores</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            compliance_rate = (compliant_count / total_records * 100) if total_records > 0 else 0
            st.markdown(f"""
            <div style="background: #d1fae5; padding: 1rem; border-radius: 0.5rem; text-align: center;">
                <div style="font-size: 2rem; font-weight: bold; color: #065f46;">{compliance_rate:.0f}%</div>
                <div style="color: #10b981; font-size: 0.875rem;">Compliance Rate</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            pending = len([c for c in compliance if c['status'] == 'Pending Review'])
            st.markdown(f"""
            <div style="background: #fef3c7; padding: 1rem; border-radius: 0.5rem; text-align: center;">
                <div style="font-size: 2rem; font-weight: bold; color: #92400e;">{pending}</div>
                <div style="color: #f59e0b; font-size: 0.875rem;">Pending Review</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            overdue = len([c for c in compliance if c['status'] == 'Action Required'])
            st.markdown(f"""
            <div style="background: #fee2e2; padding: 1rem; border-radius: 0.5rem; text-align: center;">
                <div style="font-size: 2rem; font-weight: bold; color: #991b1b;">{overdue}</div>
                <div style="color: #ef4444; font-size: 0.875rem;">Action Required</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Compliance table
        st.subheader("📋 Recent Compliance Records")
        
        # Filter by region if selected
        if selected_region != "All":
            store_ids = [s['id'] for s in stores if s['region'] == selected_region]
            filtered_compliance = [c for c in compliance if c['store_id'] in store_ids]
        else:
            filtered_compliance = compliance
        
        if filtered_compliance:
            df = pd.DataFrame(filtered_compliance)
            # Add store names
            store_map = {s['id']: s['name'] for s in stores}
            df['store_name'] = df['store_id'].map(store_map)
            
            # Reorder columns
            df_display = df[['store_name', 'category', 'status', 'last_audit', 'next_due', 'reviewer', 'notes']]
            df_display.columns = ['Store', 'Category', 'Status', 'Last Audit', 'Next Due', 'Reviewer', 'Notes']
            
            # Color coding
            def color_status(val):
                if val == 'Compliant':
                    return 'background-color: #d1fae5; color: #065f46'
                elif val == 'Pending Review':
                    return 'background-color: #fef3c7; color: #92400e'
                elif val == 'Action Required':
                    return 'background-color: #fee2e2; color: #991b1b'
                return ''
            
            st.dataframe(
                df_display.style.applymap(color_status, subset=['Status']),
                use_container_width=True,
                hide_index=True
            )
            
            # Export button
            csv = df_display.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Export to CSV",
                data=csv,
                file_name=f"compliance_report_{datetime.now().strftime('%Y-%m-%d')}.csv",
                mime="text/csv"
            )
        else:
            st.info("No compliance records found for selected filters.")
    
    with tab2:
        st.subheader("🏪 Store Management")
        
        for store in stores:
            with st.expander(f"{store['name']} - {store['region']}"):
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.write(f"**Manager:** {store['manager']}")
                    st.write(f"**Region:** {store['region']}")
                    
                    # Show compliance summary for this store
                    store_compliance = [c for c in compliance if c['store_id'] == store['id']]
                    if store_compliance:
                        compliant = len([c for c in store_compliance if c['status'] == 'Compliant'])
                        st.write(f"**Compliance:** {compliant}/{len(store_compliance)} items compliant")
                
                with col2:
                    # Mini status chart
                    if store_compliance:
                        status_counts = pd.DataFrame(store_compliance)['status'].value_counts()
                        st.bar_chart(status_counts)
    
    with tab3:
        st.subheader("➕ Add New Compliance Record")
        
        with st.form("add_compliance"):
            col1, col2 = st.columns(2)
            
            with col1:
                store_names = {s['id']: s['name'] for s in stores}
                selected_store = st.selectbox("Store", options=list(store_names.keys()), format_func=lambda x: store_names[x])
                category = st.selectbox("Compliance Category", [
                    "Fire Safety Certificate",
                    "Liquor License", 
                    "Health & Safety",
                    "COIDA Registration",
                    "Tax Clearance Certificate",
                    "BEE Certificate",
                    "Environmental Permit",
                    "Building Occupancy Certificate",
                    "Food Safety License"
                ])
            
            with col2:
                status = st.selectbox("Status", ["Compliant", "Pending Review", "Action Required"])
                last_audit = st.date_input("Last Audit Date")
                next_due = st.date_input("Next Due Date")
                reviewer = st.text_input("Reviewer/Authority")
            
            notes = st.text_area("Notes")
            
            submitted = st.form_submit_button("Add Record")
            
            if submitted:
                new_record = {
                    "id": len(compliance) + 1,
                    "store_id": selected_store,
                    "category": category,
                    "status": status,
                    "last_audit": last_audit.strftime("%Y-%m-%d"),
                    "next_due": next_due.strftime("%Y-%m-%d"),
                    "reviewer": reviewer,
                    "notes": notes
                }
                compliance.append(new_record)
                save_data(stores, compliance)
                st.success("✅ Record added successfully!")
                st.balloons()
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>🔒 Built for South African compliance standards | ForgeStack Africa © 2025</p>
        <p>Cape Town, South Africa | Contact: hello@forgestackafrica.dev</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
