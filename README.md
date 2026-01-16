# FSP Python Journey - Project Portfolio

A collection of professional Python projects built during the Full Stack Python journey. This repository serves as a personal product lab, showcasing full-stack development, automation, and data-driven tools.

## 📁 Project Structure

### 1. 🎂 [Birthday Reminder](./birthday_reminder)
Automated birthday reminder system for M&H Company employees (~100 employees).

**Features:**
- Employee management with MM-DD birthday format
- Automated daily email greetings at 8:00 AM
- Department analytics and reporting
- CSV export functionality

**Tech Stack:** Streamlit, APScheduler, SMTP

**Run:** `streamlit run birthday_reminder/app/streamlit_app.py` (Port: 8508)

**Status:** ✅ Production Ready

---

### 2. ✅ [Compliance Tracker](./compliance_tracker)
Professional compliance management system for Waterfront Mall retail stores. A lightweight compliance management tool designed to track regulatory requirements, deadlines, and completion status.

**Features:**
- Store management (CRUD operations)
- 9 compliance categories (Fire Suppression, Extraction, Liquor Licence, etc.)
- Compliance logging with status tracking
- Advanced reporting and analytics
- Professional UI with Waterfront branding

**Tech Stack:** Streamlit, Pandas, Pillow

**Run:** `streamlit run compliance_tracker/compliance_tracker.py` (Port: 8506)

**Status:** ✅ Production Ready

---

### 3. 📊 [Supplier Pricing Intelligence Tool](./supplier_pricing_intelligence_tool)
Advanced supplier pricing analysis and invoice parsing system. A full-stack pricing analysis platform that ingests supplier invoices (CSV), compares line-item prices, and identifies the cheapest supplier per product.

**Features:**
- Parse supplier invoice and pricing data from CSV files
- Line-item normalization and comparison
- Cheapest supplier identification
- Multiple format support
- Data validation and analysis
- Price insights and reporting

**Tech Stack:** Python, Pandas, FastAPI (optional)

**Run:** `python supplier_pricing_intelligence_tool/invoice_parser_v2.py`

**Status:** ✅ Complete

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment: `.venv`

### Install All Dependencies
```bash
# Birthday Reminder
cd birthday_reminder && pip install -r requirements.txt && cd ..

# Compliance Tracker
cd compliance_tracker && pip install -r requirements.txt && cd ..

# Supplier Pricing Intelligence Tool
cd supplier_pricing_intelligence_tool && pip install -r requirements.txt && cd ..
```

### Or install individually
```bash
pip install -r birthday_reminder/requirements.txt
pip install -r compliance_tracker/requirements.txt
pip install -r supplier_pricing_intelligence_tool/requirements.txt
```

---

## 📊 Project Summary

| Project | Type | Status | Port |
|---------|------|--------|------|
| Birthday Reminder | Streamlit App | ✅ Production Ready | 8508 |
| Compliance Tracker | Streamlit App | ✅ Production Ready | 8506 |
| Supplier Pricing Intelligence Tool | CLI Script | ✅ Complete | - |

---

## 🛠 Tech Stack
- Python 3.8+
- Streamlit (Web UI)
- Pandas (Data processing)
- APScheduler (Background jobs)
- FastAPI (API framework - optional)

---

## 🎯 Purpose of This Repository
- Build **real, business-driven tools**
- Demonstrate **clean architecture and full-stack thinking**
- Serve as a foundation for standalone products and future expansion
- Showcase professional Python development practices

---

## 📝 Git Commits

All projects are version controlled. View commit history:
```bash
git log --oneline
```

---

## 🤝 Contributing

Each project has its own documentation. Refer to individual README files for detailed setup and usage instructions.

---

## 🚀 Roadmap
- Extract projects into standalone repos as they mature
- Add authentication and persistence layers (PostgreSQL)
- Improve analytics and reporting features
- Deploy live demos to cloud platforms
- Add automated testing and CI/CD pipelines

---

## 📄 License
MIT License

---

**Last Updated:** January 16, 2026
