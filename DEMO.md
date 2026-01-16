# Demo & Screenshots Guide

## Quick Demo (5 Minutes)

### 1. Install & Run
```bash
make install
make run
```

The Birthday Reminder app opens at **http://localhost:8508**

### 2. Explore Features
- **Dashboard** — See upcoming birthdays this month
- **Add Employee** — Try adding a test employee
- **Manage Employees** — Search and filter employees  
- **Upcoming Birthdays** — View and export birthdays

### 3. Try Compliance Tracker
```bash
make run-compliance
```

Opens at **http://localhost:8506**

---

## Application Screenshots

### Birthday Reminder System

**Dashboard:**
- Overview metrics (Total employees, upcoming birthdays)
- Upcoming birthdays in next 30 days
- Department distribution chart
- One-click employee addition

**Key Pages:**
- 📊 Dashboard — Metrics and upcoming events
- ➕ Add Employee — Quick employee enrollment
- 📋 Manage Employees — Search, filter, sort, delete
- 🎁 Upcoming Birthdays — Export to CSV

**Data Format:** MM-DD (January 15 = "01-15")

---

### Compliance Tracker

**Dashboard:**
- Store metrics (Total, by category)
- Compliance status breakdown
- Recent audits
- Upcoming deadlines

**Key Features:**
- Store Management — Add/edit retail locations
- Compliance Logging — Track audits (Fire, Extraction, Liquor Licence, etc.)
- Records View — Advanced filtering and CSV export
- Reports — Category and store-level analytics

**Compliance Categories:**
1. Fire Suppression
2. Extraction
3. Liquor Licence
4. Business Licence
5. Pest Control
6. HACCP
7. Waste Management
8. Electrical
9. Store Front

---

### Supplier Pricing Intelligence

**Capabilities:**
- Parse supplier invoices (CSV)
- Identify cheapest supplier per product
- Compare line-item prices
- Export analysis results

**Run:**
```bash
make run-supplier
# or
python apps/supplier_pricing_intelligence_tool/invoice_parser_v2.py
```

---

## Feature Highlights

### Birthday Reminder
✅ **Automated Emails** — Runs at 8:00 AM daily  
✅ **Custom Messages** — 5 templates, randomly selected  
✅ **Privacy-First** — Stores only MM-DD (no birth year)  
✅ **Team Integration** — Department-level analytics  
✅ **Export** — CSV for HR systems  

### Compliance Tracker
✅ **Multi-Location** — Manage unlimited stores  
✅ **Audit Trail** — Track every compliance check  
✅ **Professional UI** — Custom CSS, responsive design  
✅ **Status Tracking** — Needs Review → In Progress → Compliant  
✅ **Reporting** — Category and store-level analytics  

### Supplier Pricing
✅ **Invoice Parsing** — Extract data from CSV  
✅ **Normalization** — Handle different formats  
✅ **Cost Analysis** — Find best pricing  
✅ **Extensible** — Add more analysis rules  

---

## Video Tutorial (Planned)

Would record:
1. **2-minute walkthrough** of each app
2. **Setup & installation**
3. **Key features demo**
4. **Export & integration examples**

---

## Live Demo

### Deployed Instances (Coming Soon)

- 🎂 Birthday Reminder: [Streamlit Cloud Link]
- ✅ Compliance Tracker: [Streamlit Cloud Link]
- 📊 Supplier Pricing: [Cloud Deployment]

To deploy yourself:
```bash
# Deploy to Streamlit Cloud
streamlit run apps/birthday_reminder/app/streamlit_app.py
# Then use Streamlit Cloud UI to deploy
```

---

## Sample Data

### Birthday Reminder Sample
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice@company.com",
  "department": "HR",
  "position": "Manager",
  "birthday": "01-15",
  "custom_message": "Hope your day is amazing!",
  "added_date": "2026-01-16T10:30:00"
}
```

### Compliance Tracker Sample
```json
{
  "store_id": "STORE_001",
  "category": "Fire Suppression",
  "status": "✅ Compliant",
  "inspector": "John Doe",
  "notes": "System checked and operational",
  "last_checked": "2026-01-15",
  "next_review": "2026-04-15"
}
```

### Supplier Pricing Sample
```
SUPPLIER_ID,PRODUCT_NAME,UNIT_PRICE,QUANTITY
SUP001,Widget A,10.50,100
SUP002,Widget A,9.75,100
SUP001,Gadget B,25.00,50
```

---

## Testing Workflows

### Birthday Reminder
1. Add 3+ employees with different months
2. Set one birthday to today
3. Check that app calculates days correctly
4. Export to CSV and verify format

### Compliance Tracker
1. Add 2 stores
2. Log compliance checks
3. Update status to "Needs Review"
4. Verify report shows pending items
5. Export records to CSV

### Supplier Pricing
1. Use `invoice_sample.csv` provided
2. Run parser
3. Verify cheapest supplier identified correctly

---

## Next Steps for Full Demo

**To fully showcase this portfolio:**

1. ✅ **Makefile** — `make install && make run` works
2. ✅ **Documentation** — Clear setup guide
3. ✅ **Code Quality** — CI/CD running
4. 📌 **Live Demo** — Deploy to Streamlit Cloud
5. 📌 **Screenshots** — Add 1-2 per app
6. 📌 **Video** — 2-3 minute walkthrough
7. 📌 **API** — FastAPI wrapper for integrations

---

## How Hiring Managers Will Use This

**5-Min:** Read README, see 3 real apps  
**15-Min:** Run `make install && make run`, test Birthday Reminder  
**30-Min:** Explore code structure, check out Compliance Tracker  
**1-Hour:** Deep dive into architecture, understand data flow  

---

**Each app is production-ready and can be deployed in <10 minutes.**
