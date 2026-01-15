# 🏬 Waterfront Mall Compliance Tracker

A professional compliance management system for tracking and managing store compliance across Waterfront Cape Town's retail facilities. Built with Streamlit for easy deployment and real-time monitoring.

## 📋 Overview

The Waterfront Mall Compliance Tracker streamlines compliance monitoring across multiple stores by:
- Managing store information and details
- Recording compliance checks across 11+ compliance categories
- Generating professional compliance reports
- Tracking upcoming compliance reviews
- Exporting compliance data to CSV

## ✨ Features

### 📊 Dashboard
- Real-time compliance overview with key metrics
- Store compliance status with color-coded indicators (🟢 🟡 🔴)
- Recent compliance checks feed
- At-a-glance compliance percentages

### 🏪 Store Management
- Add, view, and manage store information
- Track store location, manager, and contact details
- Store categorization (Restaurant, Retail, Pharmacy, etc.)
- Delete stores and associated records

### ✅ Compliance Logging
- Record compliance checks for multiple categories:
  - Fire Extraction
  - Food Safety
  - Liquor License
  - Building Safety
  - Health & Hygiene
  - Emergency Exits
  - Staff Training
  - Waste Management
  - Electrical Safety
  - Pest Control
  - HACCP Compliance
- Set compliance status (Passed, Failed, Needs Review, Not Applicable)
- Schedule next review dates
- Add detailed notes and findings

### 📋 Records Management
- View all compliance records with advanced filtering
- Filter by store, compliance category, or status
- Export records to CSV for reporting
- Search and organize compliance history

### 📈 Reports & Analytics
- Compliance status charts by category
- Store-level compliance summaries with percentages
- Upcoming compliance reviews (next 30 days)
- Priority-based alerts (URGENT, SOON, UPCOMING)
- Visual compliance indicators

## 🎨 Professional Design
- Waterfront Cape Town branding with logo
- Professional color scheme (Navy, teal, green)
- Responsive layout for all screen sizes
- Intuitive navigation with sidebar menu
- Status badges and visual indicators
- Custom CSS styling

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment (optional but recommended)
- Streamlit

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Burfix/fsp-python-journey.git
   cd fsp-python-journey
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit pandas
   ```

4. **Run the application**
   ```bash
   streamlit run frontend/compliance_tracker.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:8505`

## 📁 Project Structure

```
frontend/
├── compliance_tracker.py    # Main Streamlit app
├── logo.png                 # Waterfront Cape Town logo
├── app.py                   # Original supplier dashboard (alternative)
├── stores.json              # Store data (auto-generated)
└── compliance_records.json  # Compliance records (auto-generated)
```

## 💾 Data Storage

The application stores data locally in JSON format:
- `stores.json` - Store information and details
- `compliance_records.json` - Compliance check records

**Note:** These files are auto-generated in the working directory when you first run the app.

## 📊 Compliance Categories

The system tracks compliance across these categories:
1. **Fire Suppression** - Fire suppression systems compliance
2. **Extraction** - Extract systems and ventilation
3. **Liquor Licence** - Alcohol retail licensing
4. **Business Licence** - Business operation license
5. **Pest Control** - Pest management procedures
6. **HACCP** - Food safety hazard analysis
7. **Waste Management** - Proper waste disposal procedures
8. **Electrical** - Electrical systems and safety
9. **Store Front** - Store appearance and entrance compliance

## 🎯 Status Indicators

- **✅ Passed** - Full compliance achieved (Green)
- **❌ Failed** - Non-compliance identified (Red)
- **⚠️ Needs Review** - Requires attention (Yellow)
- **⊘ Not Applicable** - Category not applicable to store

## 📅 Review Scheduling

- Default review period: 90 days from last check
- Customizable review dates
- Automatic alerts for upcoming reviews
- Priority classification:
  - 🔴 **URGENT** - Due within 7 days
  - 🟡 **SOON** - Due within 14 days
  - 🟢 **UPCOMING** - Due within 30 days

## 🔍 Navigation

### Main Menu
- **📊 Dashboard** - Overview and key metrics
- **🏪 Manage Stores** - Store administration
- **✅ Log Compliance** - Record new compliance checks
- **📋 View Records** - Search and view compliance history
- **📈 Reports** - Analytics and trend reports

## 💡 Usage Tips

1. **Adding Stores First**: Start by adding all stores in "Manage Stores" before logging compliance
2. **Regular Updates**: Log compliance checks regularly to maintain accurate records
3. **Export Data**: Regularly export compliance data for backup and analysis
4. **Review Scheduling**: Set realistic review dates based on compliance requirements
5. **Documentation**: Add detailed notes for failed checks to track remediation

## 🔄 Export & Backup

- Export compliance records to CSV from the "View Records" page
- Backup JSON files regularly for data protection
- Compatible with Excel and other data analysis tools

## 🌐 Deployment Options

### Local Deployment
```bash
streamlit run frontend/compliance_tracker.py
```

### Cloud Deployment (Streamlit Cloud)
1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Set main file path to `frontend/compliance_tracker.py`

### Docker Deployment (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "frontend/compliance_tracker.py"]
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Data Storage**: JSON (local)
- **Styling**: Custom CSS
- **Python Version**: 3.8+

## 📝 Requirements

See `requirements.txt`:
```
streamlit
pandas
```

## 🐛 Troubleshooting

### App won't start
- Ensure Python 3.8+ is installed
- Activate virtual environment
- Install dependencies: `pip install -r requirements.txt`

### Logo not displaying
- Ensure `logo.png` is in the `frontend/` directory
- Check file permissions

### Data not persisting
- Check file permissions for JSON files
- Ensure write access to the working directory

## 🚀 Future Enhancements

- [ ] Database backend (PostgreSQL/MongoDB)
- [ ] User authentication and role-based access
- [ ] Email alerts for failed compliance
- [ ] Photo/document attachments
- [ ] Mobile app
- [ ] API for integration
- [ ] Advanced analytics and predictive reporting
- [ ] Compliance template management
- [ ] Multi-location dashboard

## 👥 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - Feel free to use this project for commercial and personal purposes.

## 📧 Support

For issues, suggestions, or questions:
- Open an issue on GitHub
- Contact: [Your Contact Info]

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Pandas Documentation](https://pandas.pydata.org/docs)
- [Python Official Docs](https://docs.python.org/3)

## 🙏 Acknowledgments

- Built for Waterfront Cape Town
- Inspired by compliance management best practices
- Special thanks to the Streamlit community

---

**Last Updated**: January 15, 2026  
**Version**: 1.0  
**Status**: Production Ready ✅
