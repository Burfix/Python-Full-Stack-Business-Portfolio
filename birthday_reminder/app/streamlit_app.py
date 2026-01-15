import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

st.set_page_config(page_title="M&H Birthday Reminder", layout="wide")

# Styling
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
    .section-title {
        color: #667eea;
        font-size: 1.5em;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
    }
    .upcoming-badge {
        background-color: #fef3c7;
        color: #78350f;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.85em;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "employees" not in st.session_state:
    st.session_state.employees = []

# Data file path
DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)
EMPLOYEES_FILE = DATA_DIR / "employees.json"

# Load existing data
def load_employees():
    if EMPLOYEES_FILE.exists():
        with open(EMPLOYEES_FILE, "r") as f:
            st.session_state.employees = json.load(f)

# Save data
def save_employees():
    with open(EMPLOYEES_FILE, "w") as f:
        json.dump(st.session_state.employees, f, indent=2, default=str)

# Load on startup
load_employees()

# Header
st.markdown("""
    <div class="main-header">
        <h1>🎂 M&H Birthday Reminder System</h1>
        <p>Manage employee birthdays and send personalized greetings</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar navigation
page = st.sidebar.radio("Navigation", 
    ["📊 Dashboard", "➕ Add Employee", "📋 Manage Employees", "🎁 Upcoming Birthdays"])

# ==================== DASHBOARD ====================
if page == "📊 Dashboard":
    st.markdown('<div class="section-title">📊 Dashboard Overview</div>', unsafe_allow_html=True)
    
    if not st.session_state.employees:
        st.info("ℹ️ No employees added yet. Go to 'Add Employee' to get started.")
    else:
        col1, col2, col3, col4 = st.columns(4)
        
        total_employees = len(st.session_state.employees)
        today = datetime.now().date()
        
        # Find birthdays this month
        this_month_birthdays = []
        for emp in st.session_state.employees:
            bday = datetime.strptime(emp["birthday"], "%Y-%m-%d").date()
            if bday.month == today.month:
                this_month_birthdays.append(emp)
        
        # Find upcoming birthdays (next 30 days)
        upcoming = []
        for emp in st.session_state.employees:
            bday = datetime.strptime(emp["birthday"], "%Y-%m-%d").date()
            # Calculate next birthday
            next_bday = bday.replace(year=today.year)
            if next_bday < today:
                next_bday = next_bday.replace(year=today.year + 1)
            days_until = (next_bday - today).days
            if 0 <= days_until <= 30:
                upcoming.append((emp, days_until))
        
        col1.metric("👥 Total Employees", total_employees)
        col2.metric("🎂 This Month", len(this_month_birthdays))
        col3.metric("📅 Upcoming (30 days)", len(upcoming))
        col4.metric("📧 Emails Sent Today", 0)  # Can be tracked later
        
        st.markdown("---")
        
        st.markdown('<div class="section-title">🎁 Upcoming Birthdays (Next 30 Days)</div>', unsafe_allow_html=True)
        
        if upcoming:
            upcoming_sorted = sorted(upcoming, key=lambda x: x[1])
            upcoming_data = []
            for emp, days in upcoming_sorted:
                bday = datetime.strptime(emp["birthday"], "%Y-%m-%d").date()
                next_bday = bday.replace(year=today.year)
                if next_bday < today:
                    next_bday = next_bday.replace(year=today.year + 1)
                
                if days == 0:
                    status = "🔴 TODAY!"
                elif days == 1:
                    status = "🟠 Tomorrow"
                else:
                    status = f"🟢 {days} days"
                
                upcoming_data.append({
                    "Status": status,
                    "Name": emp["name"],
                    "Department": emp["department"],
                    "Birthday": emp["birthday"],
                    "Age": datetime.now().year - datetime.strptime(emp["birthday"], "%Y-%m-%d").year
                })
            
            df_upcoming = pd.DataFrame(upcoming_data)
            st.dataframe(df_upcoming, use_container_width=True, hide_index=True)
        else:
            st.info("✅ No upcoming birthdays in the next 30 days.")
        
        st.markdown("---")
        
        st.markdown('<div class="section-title">📊 Department Distribution</div>', unsafe_allow_html=True)
        
        departments = {}
        for emp in st.session_state.employees:
            dept = emp.get("department", "Unknown")
            departments[dept] = departments.get(dept, 0) + 1
        
        if departments:
            df_dept = pd.DataFrame(list(departments.items()), columns=["Department", "Count"])
            st.bar_chart(df_dept.set_index("Department"))

# ==================== ADD EMPLOYEE ====================
elif page == "➕ Add Employee":
    st.markdown('<div class="section-title">➕ Add New Employee</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        emp_name = st.text_input("Full Name", placeholder="John Doe")
        emp_email = st.text_input("Email Address", placeholder="john@example.com")
        emp_department = st.selectbox("Department", 
            ["HR", "Sales", "Marketing", "IT", "Finance", "Operations", "Logistics", "Other"])
        emp_position = st.text_input("Position", placeholder="Manager")
    
    with col2:
        emp_birthday = st.date_input("Date of Birth")
        emp_phone = st.text_input("Phone Number", placeholder="+1 (555) 000-0000")
        emp_custom_msg = st.text_area("Custom Birthday Message (Optional)", 
            placeholder="Leave blank for default message", height=80)
    
    col_save, col_space = st.columns([1, 4])
    with col_save:
        if st.button("✅ Add Employee", use_container_width=True):
            if emp_name and emp_email:
                new_employee = {
                    "id": len(st.session_state.employees) + 1,
                    "name": emp_name,
                    "email": emp_email,
                    "department": emp_department,
                    "position": emp_position,
                    "birthday": emp_birthday.isoformat(),
                    "phone": emp_phone,
                    "custom_message": emp_custom_msg,
                    "added_date": datetime.now().isoformat()
                }
                st.session_state.employees.append(new_employee)
                save_employees()
                st.success(f"✅ Employee '{emp_name}' added successfully!")
                st.rerun()
            else:
                st.error("❌ Please fill in Name and Email fields")

# ==================== MANAGE EMPLOYEES ====================
elif page == "📋 Manage Employees":
    st.markdown('<div class="section-title">📋 Manage Employees</div>', unsafe_allow_html=True)
    
    if not st.session_state.employees:
        st.info("ℹ️ No employees added yet.")
    else:
        # Search and filter
        st.markdown("#### 🔍 Search & Filter")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_name = st.text_input("Search by name")
        with col2:
            filter_dept = st.selectbox("Filter by department", 
                ["All"] + sorted(set(e["department"] for e in st.session_state.employees)))
        with col3:
            sort_by = st.selectbox("Sort by", ["Name", "Department", "Birthday"])
        
        # Filter employees
        filtered = st.session_state.employees
        if search_name:
            filtered = [e for e in filtered if search_name.lower() in e["name"].lower()]
        if filter_dept != "All":
            filtered = [e for e in filtered if e["department"] == filter_dept]
        
        # Sort
        if sort_by == "Name":
            filtered = sorted(filtered, key=lambda x: x["name"])
        elif sort_by == "Department":
            filtered = sorted(filtered, key=lambda x: x["department"])
        elif sort_by == "Birthday":
            filtered = sorted(filtered, key=lambda x: x["birthday"])
        
        st.markdown("---")
        
        # Display employees
        display_data = []
        for emp in filtered:
            bday = datetime.strptime(emp["birthday"], "%Y-%m-%d").date()
            age = datetime.now().year - bday.year
            display_data.append({
                "Name": emp["name"],
                "Email": emp["email"],
                "Department": emp["department"],
                "Position": emp["position"],
                "Birthday": emp["birthday"],
                "Age": age,
                "Phone": emp["phone"]
            })
        
        if display_data:
            df = pd.DataFrame(display_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.markdown('<div class="section-title">🗑️ Delete Employee</div>', unsafe_allow_html=True)
        
        emp_to_delete = st.selectbox("Select employee to delete", 
            [e["name"] for e in st.session_state.employees], key="delete_emp")
        
        col_del, col_space = st.columns([1, 4])
        with col_del:
            if st.button("🗑️ Delete", use_container_width=True):
                st.session_state.employees = [e for e in st.session_state.employees if e["name"] != emp_to_delete]
                save_employees()
                st.success(f"✅ Employee '{emp_to_delete}' deleted!")
                st.rerun()

# ==================== UPCOMING BIRTHDAYS ====================
elif page == "🎁 Upcoming Birthdays":
    st.markdown('<div class="section-title">🎁 Upcoming Birthdays</div>', unsafe_allow_html=True)
    
    if not st.session_state.employees:
        st.info("ℹ️ No employees added yet.")
    else:
        # Time range selector
        col1, col2 = st.columns(2)
        with col1:
            days_ahead = st.slider("Show birthdays for the next (days):", 1, 365, 30)
        
        today = datetime.now().date()
        upcoming = []
        
        for emp in st.session_state.employees:
            bday = datetime.strptime(emp["birthday"], "%Y-%m-%d").date()
            # Calculate next birthday
            next_bday = bday.replace(year=today.year)
            if next_bday < today:
                next_bday = next_bday.replace(year=today.year + 1)
            days_until = (next_bday - today).days
            
            if 0 <= days_until <= days_ahead:
                age = next_bday.year - bday.year
                upcoming.append({
                    "Name": emp["name"],
                    "Email": emp["email"],
                    "Department": emp["department"],
                    "Birthday Date": str(next_bday),
                    "Days Until": days_until,
                    "Will Turn": age,
                    "Custom Message": "✓" if emp.get("custom_message") else "✗"
                })
        
        if upcoming:
            upcoming_sorted = sorted(upcoming, key=lambda x: x["Days Until"])
            df_upcoming = pd.DataFrame(upcoming_sorted)
            st.dataframe(df_upcoming, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            
            # Export option
            csv = df_upcoming.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"upcoming_birthdays_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.info(f"✅ No birthdays in the next {days_ahead} days.")

st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em; margin-top: 2rem;">
        <p>🎂 <strong>M&H Birthday Reminder System</strong></p>
        <p>Celebrate your team members! v1.0</p>
    </div>
""", unsafe_allow_html=True)
