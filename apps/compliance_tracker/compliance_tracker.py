import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
import json

st.set_page_config(
    page_title="Waterfront Mall Compliance Tracker",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://waterfront-mall.local",
        "About": "Compliance Management System v1.0"
    }
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    /* Main theme colors */
    :root {
        --primary-color: #1e3a5f;
        --secondary-color: #2d5a8c;
        --accent-color: #00a86b;
        --danger-color: #dc2626;
        --warning-color: #f59e0b;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a8c 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5em;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-size: 1.1em;
    }
    
    /* Metrics styling */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #1e3a5f;
    }
    
    /* Status badges */
    .status-passed {
        background-color: #d1fae5;
        color: #065f46;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.85em;
    }
    
    .status-failed {
        background-color: #fee2e2;
        color: #7f1d1d;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.85em;
    }
    
    .status-review {
        background-color: #fef3c7;
        color: #78350f;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.85em;
    }
    
    /* Section titles */
    .section-title {
        color: #1e3a5f;
        font-size: 1.5em;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #00a86b;
        padding-bottom: 0.5rem;
    }
    
    /* Form styling */
    .form-section {
        background: #f8fafc;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #00a86b;
    }
    
    /* Data table styling */
    .dataframe {
        font-size: 0.95em;
    }
    
    .stDataFrame {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #00a86b;
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.5rem;
    }
    
    .stButton > button:hover {
        background-color: #008c56;
    }
    
    .danger-button > button {
        background-color: #dc2626;
    }
    
    .danger-button > button:hover {
        background-color: #b91c1c;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
    }
    
    /* Alert boxes */
    .info-box {
        background-color: #dbeafe;
        border-left: 4px solid #0284c7;
        padding: 1rem;
        border-radius: 6px;
    }
    
    .success-box {
        background-color: #d1fae5;
        border-left: 4px solid #10b981;
        padding: 1rem;
        border-radius: 6px;
    }
    
    .error-box {
        background-color: #fee2e2;
        border-left: 4px solid #ef4444;
        padding: 1rem;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "stores" not in st.session_state:
    st.session_state.stores = []
if "compliance_records" not in st.session_state:
    st.session_state.compliance_records = []

# Data file paths
STORES_FILE = "stores.json"
COMPLIANCE_FILE = "compliance_records.json"

# Load existing data
def load_data():
    if os.path.exists(STORES_FILE):
        with open(STORES_FILE, "r") as f:
            st.session_state.stores = json.load(f)
    if os.path.exists(COMPLIANCE_FILE):
        with open(COMPLIANCE_FILE, "r") as f:
            st.session_state.compliance_records = json.load(f)

# Save data
def save_data():
    with open(STORES_FILE, "w") as f:
        json.dump(st.session_state.stores, f, indent=2, default=str)
    with open(COMPLIANCE_FILE, "w") as f:
        json.dump(st.session_state.compliance_records, f, indent=2, default=str)

# Compliance categories
COMPLIANCE_CATEGORIES = [
    "Fire Suppression",
    "Extraction",
    "Liquor Licence",
    "Business Licence",
    "Pest Control",
    "HACCP",
    "Waste Management",
    "Electrical",
    "Store Front"
]

# Load data on app start
load_data()

# Professional header with Waterfront Cape Town logo
import os
col_logo, col_title = st.columns([1, 5])

with col_logo:
    logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, width=100)
    else:
        st.write("🏬")

with col_title:
    st.markdown("""
        <div class="main-header">
            <h1>🏬 Waterfront Mall Compliance Tracker</h1>
            <p>Waterfront Cape Town | Professional Compliance Management System</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Sidebar navigation
page = st.sidebar.radio("Navigation", 
    ["📊 Dashboard", "🏪 Manage Stores", "✅ Log Compliance", "📋 View Records", "📈 Reports"])

# ==================== DASHBOARD ====================
if page == "📊 Dashboard":
    st.markdown('<div class="section-title">📊 Compliance Dashboard</div>', unsafe_allow_html=True)
    
    if not st.session_state.stores:
        st.info("ℹ️ No stores added yet. Go to 'Manage Stores' to add stores.")
    else:
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        
        total_stores = len(st.session_state.stores)
        total_checks = len(st.session_state.compliance_records)
        
        # Calculate compliance status
        passed = len([r for r in st.session_state.compliance_records if r["status"] == "Passed"])
        failed = len([r for r in st.session_state.compliance_records if r["status"] == "Failed"])
        
        col1.metric("📍 Total Stores", total_stores, help="Number of registered stores")
        col2.metric("✅ Total Checks", total_checks, help="Total compliance checks performed")
        col3.metric("✓ Passed", passed, delta_color="off", help="Checks that passed compliance")
        col4.metric("✗ Failed", failed, delta_color="inverse", help="Checks that failed compliance")
        
        st.markdown("---")
        
        # Compliance status by store
        st.markdown('<div class="section-title">Store Compliance Status</div>', unsafe_allow_html=True)
        
        store_status = []
        for store in st.session_state.stores:
            store_records = [r for r in st.session_state.compliance_records if r["store_id"] == store["id"]]
            if store_records:
                passed_count = len([r for r in store_records if r["status"] == "Passed"])
                total_count = len(store_records)
                completion_rate = (passed_count / total_count * 100) if total_count > 0 else 0
            else:
                completion_rate = 0
                total_count = 0
                passed_count = 0
            
            # Color code compliance percentage
            if completion_rate >= 80:
                status_emoji = "🟢"
            elif completion_rate >= 50:
                status_emoji = "🟡"
            else:
                status_emoji = "🔴"
            
            store_status.append({
                "Status": status_emoji,
                "Store Name": store["name"],
                "Category": store["category"],
                "Passed": passed_count,
                "Total Checks": total_count,
                "Compliance %": f"{completion_rate:.0f}%"
            })
        
        if store_status:
            df_status = pd.DataFrame(store_status)
            st.dataframe(df_status, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Recent compliance checks
        st.markdown('<div class="section-title">Recent Compliance Checks</div>', unsafe_allow_html=True)
        if st.session_state.compliance_records:
            recent_records = sorted(st.session_state.compliance_records, 
                                  key=lambda x: x["date"], reverse=True)[:10]
            
            recent_df_data = []
            for record in recent_records:
                store_name = next((s["name"] for s in st.session_state.stores if s["id"] == record["store_id"]), "Unknown")
                status_emoji = "✅" if record["status"] == "Passed" else "❌" if record["status"] == "Failed" else "⚠️"
                recent_df_data.append({
                    "": status_emoji,
                    "Date": record["date"],
                    "Store": store_name,
                    "Category": record["category"],
                    "Status": record["status"],
                    "Notes": record["notes"][:50] + "..." if len(record["notes"]) > 50 else record["notes"]
                })
            
            df_recent = pd.DataFrame(recent_df_data)
            st.dataframe(df_recent, use_container_width=True, hide_index=True)

# ==================== MANAGE STORES ====================
elif page == "🏪 Manage Stores":
    st.markdown('<div class="section-title">🏪 Manage Stores</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="form-section">', unsafe_allow_html=True)
        st.markdown("#### ➕ Add New Store")
        
        store_name = st.text_input("Store Name", key="store_name", placeholder="e.g., Fresh & Co")
        store_category = st.selectbox("Store Category", 
            ["Restaurant", "Retail", "Pharmacy", "Bakery", "Bar/Lounge", "Cafe", "Fast Food", "Other"])
        store_location = st.text_input("Store Location/Unit", key="store_location", placeholder="e.g., Level 2, Unit 205")
        store_manager = st.text_input("Manager Name", key="store_manager", placeholder="Full name")
        store_phone = st.text_input("Contact Phone", key="store_phone", placeholder="+1 (555) 000-0000")
        
        col_add, col_space = st.columns([1, 4])
        with col_add:
            if st.button("✅ Add Store", key="add_store_btn", use_container_width=True):
                if store_name:
                    new_store = {
                        "id": len(st.session_state.stores) + 1,
                        "name": store_name,
                        "category": store_category,
                        "location": store_location,
                        "manager": store_manager,
                        "phone": store_phone,
                        "added_date": datetime.now().isoformat()
                    }
                    st.session_state.stores.append(new_store)
                    save_data()
                    st.success(f"✅ Store '{store_name}' added successfully!")
                    st.rerun()
                else:
                    st.error("❌ Please enter store name")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.write("")  # Spacing
    
    st.markdown("---")
    
    st.markdown('<div class="section-title">📋 Existing Stores</div>', unsafe_allow_html=True)
    if st.session_state.stores:
        df_stores = pd.DataFrame(st.session_state.stores)
        st.dataframe(df_stores[["name", "category", "location", "manager", "phone"]], 
                    use_container_width=True, hide_index=True)
        
        st.markdown("---")
        st.markdown('<div class="section-title">🗑️ Delete Store</div>', unsafe_allow_html=True)
        col_select, col_btn = st.columns([3, 1])
        with col_select:
            store_to_delete = st.selectbox("Select store to delete", 
                [s["name"] for s in st.session_state.stores], key="delete_select")
        with col_btn:
            if st.button("🗑️ Delete", key="delete_store_btn", use_container_width=True):
                st.session_state.stores = [s for s in st.session_state.stores if s["name"] != store_to_delete]
                save_data()
                st.success(f"✅ Store '{store_to_delete}' deleted!")
                st.rerun()
    else:
        st.info("ℹ️ No stores added yet.")

# ==================== LOG COMPLIANCE ====================
elif page == "✅ Log Compliance":
    st.markdown('<div class="section-title">✅ Log Compliance Check</div>', unsafe_allow_html=True)
    
    if not st.session_state.stores:
        st.error("❌ No stores available. Please add stores first in 'Manage Stores'.")
    else:
        st.markdown('<div class="form-section">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            selected_store = st.selectbox("Select Store", 
                [s["name"] for s in st.session_state.stores], key="log_store")
            store_id = next(s["id"] for s in st.session_state.stores if s["name"] == selected_store)
            
            compliance_category = st.selectbox("Compliance Category", COMPLIANCE_CATEGORIES, key="log_category")
            
            compliance_status = st.radio("Compliance Status", 
                ["✅ Passed", "❌ Failed", "⚠️ Needs Review", "⊘ Not Applicable"], 
                key="log_status", horizontal=False)
        
        with col2:
            check_date = st.date_input("Check Date", value=datetime.now())
            
            next_review_date = st.date_input("Next Review Due", 
                value=datetime.now() + timedelta(days=90))
            
            inspector_name = st.text_input("Inspector Name", key="log_inspector", placeholder="Full name")
        
        compliance_notes = st.text_area("Notes/Findings", key="log_notes", height=100, 
                                       placeholder="Document any findings, issues, or observations...")
        
        col_save, col_space = st.columns([1, 4])
        with col_save:
            if st.button("💾 Save Record", key="save_compliance_btn", use_container_width=True):
                if inspector_name:
                    # Extract status properly - remove emoji and trim whitespace
                    status_clean = compliance_status.split(" ", 1)[1] if " " in compliance_status else compliance_status
                    new_record = {
                        "id": len(st.session_state.compliance_records) + 1,
                        "store_id": store_id,
                        "category": compliance_category,
                        "status": status_clean,
                        "date": check_date.isoformat(),
                        "next_review": next_review_date.isoformat(),
                        "inspector": inspector_name,
                        "notes": compliance_notes,
                        "logged_at": datetime.now().isoformat()
                    }
                    st.session_state.compliance_records.append(new_record)
                    save_data()
                    st.success(f"✅ Compliance record for '{selected_store}' saved successfully!")
                    st.rerun()
                else:
                    st.error("❌ Please enter inspector name")
        
        st.markdown("</div>", unsafe_allow_html=True)

# ==================== VIEW RECORDS ====================
elif page == "📋 View Records":
    st.markdown('<div class="section-title">📋 Compliance Records</div>', unsafe_allow_html=True)
    
    if not st.session_state.compliance_records:
        st.info("ℹ️ No compliance records yet.")
    else:
        # Filters
        st.markdown("#### 🔍 Filter Records")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_store = st.selectbox("Filter by Store", 
                ["All"] + [s["name"] for s in st.session_state.stores], key="view_filter_store")
        
        with col2:
            filter_category = st.selectbox("Filter by Category", 
                ["All"] + COMPLIANCE_CATEGORIES, key="view_filter_category")
        
        with col3:
            filter_status = st.selectbox("Filter by Status", 
                ["All", "Passed", "Failed", "Needs Review", "Not Applicable"], key="view_filter_status")
        
        st.markdown("---")
        
        # Apply filters
        filtered_records = st.session_state.compliance_records
        
        if filter_store != "All":
            store_id = next(s["id"] for s in st.session_state.stores if s["name"] == filter_store)
            filtered_records = [r for r in filtered_records if r["store_id"] == store_id]
        
        if filter_category != "All":
            filtered_records = [r for r in filtered_records if r["category"] == filter_category]
        
        if filter_status != "All":
            filtered_records = [r for r in filtered_records if r["status"] == filter_status]
        
        # Display records
        if filtered_records:
            display_records = []
            for record in filtered_records:
                store_name = next((s["name"] for s in st.session_state.stores if s["id"] == record["store_id"]), "Unknown")
                status_emoji = "✅" if record["status"] == "Passed" else "❌" if record["status"] == "Failed" else "⚠️"
                display_records.append({
                    "": status_emoji,
                    "Date": record["date"],
                    "Store": store_name,
                    "Category": record["category"],
                    "Status": record["status"],
                    "Inspector": record["inspector"],
                    "Next Review": record["next_review"]
                })
            
            df_records = pd.DataFrame(display_records)
            st.dataframe(df_records, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            st.markdown("#### 📥 Export")
            
            # Export option
            csv_data = df_records.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv_data,
                file_name=f"compliance_records_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.info("ℹ️ No records match the selected filters.")

# ==================== REPORTS ====================
elif page == "📈 Reports":
    st.markdown('<div class="section-title">📈 Compliance Reports</div>', unsafe_allow_html=True)
    
    if not st.session_state.compliance_records:
        st.info("ℹ️ No data available for reports.")
    else:
        # Compliance by category
        st.markdown("#### 📊 Compliance Status by Category")
        
        category_stats = {}
        for record in st.session_state.compliance_records:
            cat = record["category"]
            status = record.get("status", "Unknown")
            if cat not in category_stats:
                category_stats[cat] = {"Passed": 0, "Failed": 0, "Needs Review": 0, "Not Applicable": 0}
            # Only add if status exists in the dictionary, otherwise skip or add to Unknown
            if status in category_stats[cat]:
                category_stats[cat][status] += 1
            else:
                # If status is not in predefined list, add it
                if status not in category_stats[cat]:
                    category_stats[cat][status] = 0
                category_stats[cat][status] += 1
        
        if category_stats:
            df_cat = pd.DataFrame(category_stats).fillna(0).astype(int)
            st.bar_chart(df_cat)
            st.dataframe(df_cat, use_container_width=True)
        
        st.markdown("---")
        
        # Compliance by store
        st.markdown("#### 🏪 Compliance Summary by Store")
        
        store_stats = {}
        for store in st.session_state.stores:
            store_records = [r for r in st.session_state.compliance_records if r["store_id"] == store["id"]]
            if store_records:
                passed = len([r for r in store_records if r["status"] == "Passed"])
                failed = len([r for r in store_records if r["status"] == "Failed"])
                total = len(store_records)
                compliance_pct = round((passed / total * 100), 1) if total > 0 else 0
                
                # Add status indicator
                if compliance_pct >= 80:
                    status = "🟢 Excellent"
                elif compliance_pct >= 60:
                    status = "🟡 Good"
                else:
                    status = "🔴 Needs Attention"
                
                store_stats[store["name"]] = {
                    "Status": status,
                    "Passed": passed,
                    "Failed": failed,
                    "Needs Review": len([r for r in store_records if r["status"] == "Needs Review"]),
                    "Total": total,
                    "Compliance %": compliance_pct
                }
        
        if store_stats:
            df_store_stats = pd.DataFrame(store_stats).T
            st.dataframe(df_store_stats, use_container_width=True)
        
        st.markdown("---")
        
        # Upcoming reviews
        st.markdown("#### 📅 Upcoming Compliance Reviews (Next 30 Days)")
        
        today = datetime.now().date()
        upcoming = []
        
        for record in st.session_state.compliance_records:
            next_review = datetime.fromisoformat(record["next_review"]).date()
            days_until = (next_review - today).days
            
            if 0 <= days_until <= 30:
                store_name = next((s["name"] for s in st.session_state.stores if s["id"] == record["store_id"]), "Unknown")
                
                if days_until <= 7:
                    priority = "🔴 URGENT"
                elif days_until <= 14:
                    priority = "🟡 SOON"
                else:
                    priority = "🟢 UPCOMING"
                
                upcoming.append({
                    "Priority": priority,
                    "Store": store_name,
                    "Category": record["category"],
                    "Due Date": record["next_review"],
                    "Days Until": days_until
                })
        
        if upcoming:
            df_upcoming = pd.DataFrame(upcoming).sort_values("Days Until")
            st.dataframe(df_upcoming, use_container_width=True, hide_index=True)
        else:
            st.info("✅ No reviews due in the next 30 days.")

st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em; margin-top: 2rem;">
        <p>🏬 <strong>Waterfront Mall Compliance Tracker</strong></p>
        <p>Professional Compliance Management System v1.0 | Data saved locally</p>
    </div>
""", unsafe_allow_html=True)
