# 🎂 M&H Birthday Reminder System

A comprehensive birthday management and automated greeting system for M&H Company. Manage up to 100+ employees' birthdays and automatically send personalized birthday greetings every morning at 8 AM.

## 🎯 Features

### 📊 Dashboard
- Real-time overview of all birthdays
- Upcoming birthdays in the next 30 days
- Monthly birthday count
- Department distribution analytics
- Quick stats on total employees and upcoming celebrations

### 👥 Employee Management
- Add, view, and manage employee information
- Track employee details: name, email, department, position, phone
- Set custom birthday messages per employee
- Search and filter employees
- Sort by name, department, or birthday
- Export employee data to CSV

### 🎁 Birthday Tracking
- View upcoming birthdays with customizable time ranges
- See which employees have custom birthday messages
- Track upcoming age milestones
- Export upcoming birthday lists

### 📧 Automated Birthday Greetings
- Scheduled daily checks at 8:00 AM
- Personalized messages with employee names
- 5 different message templates for variety:
  - Default: Professional and warm
  - Professional: Business-appropriate
  - Warm: Personal and heartfelt
  - Fun: Light-hearted and celebratory
  - Heartfelt: Emotional and sincere
- Support for custom messages per employee
- Email delivery via SMTP

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- Email account (Gmail or corporate email with SMTP access)

### Installation

1. **Clone or extract the project**
   ```bash
   cd /Users/Thami/fsp-python-journey/birthday_reminder
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup configuration**
   ```bash
   cp config.json.example config.json
   ```

5. **Configure SMTP settings in `config.json`**
   ```json
   {
     "smtp": {
       "smtp_server": "smtp.gmail.com",
       "smtp_port": 587,
       "sender_email": "your-email@gmail.com",
       "sender_password": "your-app-password",
       "from_name": "M&H Birthday Reminder"
     }
   }
   ```

### Running the Application

#### Option 1: Streamlit Frontend Only
```bash
streamlit run app/streamlit_app.py
```
Access at: `http://localhost:8501`

#### Option 2: With Background Scheduler
```bash
python scheduler/birthday_scheduler.py
```
(In another terminal, run the Streamlit app)

## 📋 Data Structure

### Employee Record
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "department": "Sales",
  "position": "Manager",
  "birthday": "1990-05-15",
  "phone": "+1 (555) 000-0000",
  "custom_message": "Custom birthday message (optional)",
  "added_date": "2026-01-15T10:30:00"
}
```

### Email Configuration
```json
{
  "smtp": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "company@gmail.com",
    "sender_password": "app-specific-password",
    "from_name": "M&H Birthday Reminder"
  }
}
```

## 📧 Gmail Setup Instructions

### Enable Less Secure Apps (if using personal Gmail)
1. Go to https://myaccount.google.com/security
2. Enable "Less secure app access"

### Use App Password (Recommended)
1. Enable 2-Factor Authentication on your Google Account
2. Go to https://myaccount.google.com/apppasswords
3. Create an "App password" for "Mail"
4. Use this password in `config.json`

## 🎨 Application Pages

### 📊 Dashboard
- Overview of all birthday information
- Quick metrics and statistics
- Upcoming birthdays list
- Department distribution chart

### ➕ Add Employee
- Form to add new employees
- Fields: Name, Email, Department, Position, Birthday, Phone, Custom Message
- Real-time data persistence

### 📋 Manage Employees
- View all employees in a table
- Search by name
- Filter by department
- Sort by name, department, or birthday
- Delete employees
- Export to CSV

### 🎁 Upcoming Birthdays
- Customizable time range (1-365 days)
- Detailed upcoming birthday list
- Age at next birthday
- Custom message indicator
- Export functionality

## 🔄 Scheduler Features

### Automatic Birthday Detection
- Checks every day at 8:00 AM
- Identifies employees with birthdays today
- Calculates current age

### Message Personalization
- Uses employee's custom message if available
- Falls back to random template for variety
- Includes employee name in greeting

### Email Delivery
- SMTP-based email sending
- Error handling and logging
- Retry capability
- Detailed logging for tracking

## 🛠️ Configuration Options

### SMTP Server Examples

**Gmail:**
```json
"smtp_server": "smtp.gmail.com",
"smtp_port": 587
```

**Outlook:**
```json
"smtp_server": "smtp.outlook.com",
"smtp_port": 587
```

**Corporate Email:**
```json
"smtp_server": "mail.company.com",
"smtp_port": 587 or 465
```

### Message Send Time
Default: 8:00 AM (Africa/Johannesburg timezone)
- Edit `scheduler/birthday_scheduler.py` CronTrigger to change
- Supports any valid timezone

## 📊 Employee Capacity

- **Tested**: Up to 100+ employees
- **Scalability**: JSON-based storage for simplicity
- **Migration Path**: Can upgrade to PostgreSQL/MongoDB for larger deployments
- **Performance**: Email sends happen in background (non-blocking)

## 🔍 Troubleshooting

### Emails not sending
1. Check `config.json` SMTP settings
2. Verify sender email and password
3. Check email account security settings
4. Look at console logs for error messages

### Streamlit app won't start
1. Ensure all dependencies installed: `pip install -r requirements.txt`
2. Check Python version (3.8+)
3. Verify virtual environment is activated

### Scheduler not running
1. Ensure APScheduler is installed
2. Check for port conflicts
3. Review console logs for errors
4. Verify config.json exists

## 📈 Future Enhancements

- [ ] SMS birthday notifications
- [ ] Slack integration
- [ ] Teams integration
- [ ] Calendar export (iCal)
- [ ] Birthday gift tracking
- [ ] Team celebration photos gallery
- [ ] Database backend (PostgreSQL)
- [ ] Docker containerization
- [ ] Email templates UI builder
- [ ] Birthday analytics dashboard
- [ ] Multi-language support
- [ ] Holiday calendar awareness

## 🔐 Security Considerations

1. **Never commit `config.json`** with real credentials
2. Use **app-specific passwords** instead of account password
3. Store credentials in **environment variables** for production
4. Use `.gitignore` to exclude sensitive files:
   ```
   config.json
   data/
   .env
   ```

## 📝 Environment Variables (Alternative to config.json)

```bash
export SMTP_SERVER=smtp.gmail.com
export SMTP_PORT=587
export SMTP_EMAIL=your-email@gmail.com
export SMTP_PASSWORD=your-app-password
```

## 🤝 Usage Examples

### Add 100 Employees
1. Use "Add Employee" page to input employees one by one
2. Or prepare a CSV and import (can be added as feature)

### Send Test Email
```bash
python scheduler/birthday_scheduler.py
```
The scheduler will check and send emails immediately on start.

### Export Employee List
1. Go to "Manage Employees"
2. Use the download button to export as CSV

### Filter Upcoming Birthdays
1. Go to "Upcoming Birthdays"
2. Set the time range slider (default 30 days)
3. View filtered results

## 📞 Support

For issues or questions:
- Check logs in console output
- Review error messages in Streamlit
- Verify SMTP configuration
- Check email account permissions

## 📄 License

This project is created for M&H Company internal use.

## 🎉 Acknowledgments

- Built with Streamlit for easy UI management
- Powered by APScheduler for reliable scheduling
- Designed with employee celebration in mind

---

**Version**: 1.0  
**Created**: January 15, 2026  
**Status**: Production Ready ✅  
**Support Capacity**: 100+ employees  
**Email Delivery**: Daily at 8:00 AM
