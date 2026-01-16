# Development Guide

## Project Overview

This portfolio contains 3 production-ready applications:

1. **Birthday Reminder** — Employee engagement automation
2. **Compliance Tracker** — Regulatory audit management  
3. **Supplier Pricing Intelligence** — Cost analysis platform

---

## Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment

### Setup (5 minutes)

```bash
# Clone repository
git clone https://github.com/Burfix/Python-Full-Stack-Business-Portfolio.git
cd Python-Full-Stack-Business-Portfolio

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install all dependencies
make install

# Run main app (Birthday Reminder)
make run
```

Or run individual apps:
```bash
make run-birthday      # Port 8508
make run-compliance    # Port 8506
make run-supplier      # CLI tool
```

---

## Repository Structure

```
.
├── apps/
│   ├── birthday_reminder/          # Streamlit + APScheduler
│   ├── compliance_tracker/         # Streamlit + Pandas
│   └── supplier_pricing_intelligence_tool/  # CLI + Pandas
├── playground/                     # Learning code (not in portfolio)
├── data/
│   └── sample_data/               # Sample datasets
├── .github/
│   └── workflows/                 # CI/CD pipelines
├── Makefile                       # Quick commands
├── README.md                      # Main documentation
└── DEVELOPMENT.md                 # This file
```

---

## Each App's Tech Stack

### 1. Birthday Reminder
- **Framework:** Streamlit (UI)
- **Background:** APScheduler (8 AM daily emails)
- **Data:** JSON file storage
- **Email:** SMTP (Gmail, Outlook, corporate)
- **Port:** 8508
- **Setup:** `make run-birthday`

**Key Files:**
- `apps/birthday_reminder/app/streamlit_app.py` — UI dashboard
- `apps/birthday_reminder/scheduler/birthday_scheduler.py` — Background job
- `apps/birthday_reminder/config.json.example` — SMTP configuration

### 2. Compliance Tracker
- **Framework:** Streamlit (UI)
- **Data:** JSON + Pandas for analytics
- **Branding:** Custom CSS + Waterfront logo
- **Port:** 8506
- **Setup:** `make run-compliance`

**Key Files:**
- `apps/compliance_tracker/compliance_tracker.py` — Main app
- `apps/compliance_tracker/data/` — Sample store & compliance data

### 3. Supplier Pricing Intelligence
- **Language:** Pure Python
- **Data:** Pandas (CSV, JSON)
- **CLI:** Command-line interface
- **Setup:** `make run-supplier`

**Key Files:**
- `apps/supplier_pricing_intelligence_tool/invoice_parser_v2.py` — Main script
- `apps/supplier_pricing_intelligence_tool/invoice_sample.csv` — Sample data

---

## Development Workflow

### Running Tests
```bash
make test         # Import tests
make lint         # Code style checks
make check        # All checks
```

### Adding a New Feature

1. Create a branch:
   ```bash
   git checkout -b feature/my-feature
   ```

2. Make changes to the relevant app in `apps/`

3. Test locally:
   ```bash
   make run-{app-name}
   ```

4. Commit with clear message:
   ```bash
   git add .
   git commit -m "feat: Add feature to {app-name}"
   ```

5. Push and open PR:
   ```bash
   git push origin feature/my-feature
   ```

---

## Configuration

### Birthday Reminder SMTP Setup

Copy `config.json.example` to `config.json` and add your SMTP credentials:

```json
{
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587,
  "sender_email": "your-email@gmail.com",
  "sender_password": "your-app-password"
}
```

For Gmail: [Generate app password](https://myaccount.google.com/apppasswords)

### Compliance Tracker Logo

Edit the logo path in `compliance_tracker.py` line ~45:
```python
logo = Image.open("path/to/your/logo.png")
```

---

## Debugging

### App Won't Start

```bash
# Clear Streamlit cache
rm -rf ~/.streamlit/

# Reinstall dependencies
pip install --upgrade -r apps/{app}/requirements.txt

# Run with verbose output
streamlit run --logger.level=debug apps/{app}/app.py
```

### Import Errors

```bash
# Verify Python path
python -c "import sys; print(sys.executable)"

# Check installed packages
pip list | grep -E "streamlit|pandas|apscheduler"
```

### Port Already in Use

```bash
# Run on different port
streamlit run apps/birthday_reminder/app/streamlit_app.py --server.port=8509
```

---

## Deployment

### Option 1: Streamlit Cloud
1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo and select app file
4. Deploy

### Option 2: Docker
```bash
docker build -t portfolio .
docker run -p 8508:8508 portfolio
```

### Option 3: AWS Lambda (Compliance Tracker)
Convert to AWS Lambda handler for serverless deployment.

---

## Git Workflow

### View Commit History
```bash
git log --oneline -10
git log --graph --all --oneline
```

### Undo Changes
```bash
git diff                    # See changes
git restore {file}          # Revert file
git reset --hard origin/main # Reset everything
```

---

## Code Style

We follow PEP 8. Run linting:

```bash
pip install flake8 black
flake8 apps/
black apps/ --line-length=100
```

---

## Performance Tips

### Streamlit Caching
```python
@st.cache_data
def load_data():
    return pd.read_json("data.json")
```

### Pandas Optimization
```python
# For large files
pd.read_csv("file.csv", dtype={'id': 'int32'})
```

---

## Troubleshooting CI/CD

Check GitHub Actions:
```
Your Repo → Actions → Quality Checks
```

---

## Contributing

1. Fork the repo
2. Create feature branch
3. Make changes
4. Run `make check`
5. Commit with clear message
6. Push and open PR

---

## Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [Pandas Docs](https://pandas.pydata.org)
- [APScheduler Docs](https://apscheduler.readthedocs.io)
- [Python PEP 8](https://pep8.org)

---

**Questions?** Open an issue on GitHub.
