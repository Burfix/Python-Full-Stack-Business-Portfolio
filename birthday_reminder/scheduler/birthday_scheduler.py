import json
import smtplib
from datetime import datetime
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import atexit

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
DATA_DIR = Path(__file__).parent.parent / "data"
EMPLOYEES_FILE = DATA_DIR / "employees.json"
CONFIG_FILE = Path(__file__).parent.parent / "config.json"

# Email templates
BIRTHDAY_TEMPLATES = {
    "default": """
Dear {name},

Wishing you a wonderful birthday and a fantastic year ahead!

Thank you for being an amazing part of the M&H team. Your contributions and dedication are truly appreciated.

Enjoy your special day! 🎂🎉

Warm regards,
M&H Company
""",
    "professional": """
Hi {name},

Happy Birthday! 🎉

We hope you have a wonderful day filled with joy, laughter, and good times.
Thank you for your continued hard work and dedication to M&H Company.

Best wishes,
The M&H Team
""",
    "warm": """
{name},

Happy Birthday to a wonderful colleague and friend!

Your positive attitude and hard work make M&H a better place every day.
We wish you all the best on your special day and always.

Cheers to you! 🥳

Best,
M&H Family
""",
    "fun": """
🎂 HAPPY BIRTHDAY, {name}! 🎂

Another year older, but definitely not wiser (just joking! 😄).

We appreciate you and everything you do. Now go enjoy your day, treat yourself, 
and come back refreshed and ready to keep crushing it!

The M&H Squad
""",
    "heartfelt": """
Dear {name},

On your birthday, we want you to know how much you mean to our M&H family.

Your kindness, professionalism, and positive energy make our workplace special.
Thank you for everything you do!

Wishing you a day as wonderful as you are.

Warmly,
Your M&H Team
"""
}

class BirthdayReminder:
    def __init__(self, smtp_config=None):
        """
        Initialize the birthday reminder service.
        
        Args:
            smtp_config: Dictionary with email configuration
                {
                    "smtp_server": "smtp.gmail.com",
                    "smtp_port": 587,
                    "sender_email": "your-email@gmail.com",
                    "sender_password": "your-password"
                }
        """
        self.smtp_config = smtp_config or self.load_config()
        self.scheduler = BackgroundScheduler()
        
    @staticmethod
    def load_config():
        """Load SMTP configuration from config file."""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, "r") as f:
                return json.load(f).get("smtp", {})
        return {}
    
    @staticmethod
    def load_employees():
        """Load employee data from JSON file."""
        if EMPLOYEES_FILE.exists():
            with open(EMPLOYEES_FILE, "r") as f:
                return json.load(f)
        return []
    
    @staticmethod
    def get_random_template():
        """Get a random birthday template for variety."""
        import random
        templates = list(BIRTHDAY_TEMPLATES.values())
        return random.choice(templates)
    
    def send_email(self, to_email, subject, body):
        """Send email to recipient."""
        if not self.smtp_config:
            logger.warning("SMTP configuration not set. Email not sent.")
            return False
        
        try:
            msg = MIMEMultipart()
            msg["From"] = self.smtp_config.get("sender_email")
            msg["To"] = to_email
            msg["Subject"] = subject
            
            msg.attach(MIMEText(body, "plain"))
            
            server = smtplib.SMTP(
                self.smtp_config.get("smtp_server", "smtp.gmail.com"),
                self.smtp_config.get("smtp_port", 587)
            )
            server.starttls()
            server.login(
                self.smtp_config.get("sender_email"),
                self.smtp_config.get("sender_password")
            )
            
            server.send_message(msg)
            server.quit()
            
            logger.info(f"✅ Birthday email sent to {to_email}")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to send email to {to_email}: {str(e)}")
            return False
    
    def check_and_send_birthdays(self):
        """Check for today's birthdays and send greetings."""
        today = datetime.now().date()
        employees = self.load_employees()
        
        logger.info(f"Checking for birthdays on {today}...")
        
        for emp in employees:
            try:
                bday_month, bday_day = map(int, emp["birthday"].split("-"))
                
                # Check if today is their birthday (month and day only)
                if bday_month == today.month and bday_day == today.day:
                    # Use custom message or random template
                    if emp.get("custom_message"):
                        message_body = emp["custom_message"].format(name=emp["name"])
                    else:
                        template = self.get_random_template()
                        message_body = template.format(name=emp["name"])
                    
                    subject = f"🎂 Happy Birthday, {emp['name']}!"
                    
                    # Send email
                    self.send_email(emp["email"], subject, message_body)
                    
                    logger.info(f"🎉 Birthday greeting sent to {emp['name']}")
            except Exception as e:
                logger.error(f"Error processing {emp.get('name')}: {str(e)}")
    
    def start(self):
        """Start the background scheduler."""
        # Schedule daily check at 8:00 AM
        self.scheduler.add_job(
            self.check_and_send_birthdays,
            CronTrigger(hour=8, minute=0),
            id="birthday_check",
            name="Daily birthday check"
        )
        
        self.scheduler.start()
        logger.info("✅ Birthday reminder scheduler started!")
        
        # Shutdown scheduler on exit
        atexit.register(lambda: self.scheduler.shutdown())
    
    def stop(self):
        """Stop the scheduler."""
        if self.scheduler.running:
            self.scheduler.shutdown()
            logger.info("⛔ Birthday reminder scheduler stopped.")


# Standalone function for testing
def test_birthday_reminder():
    """Test function to send a birthday reminder manually."""
    reminder = BirthdayReminder()
    reminder.check_and_send_birthdays()


if __name__ == "__main__":
    # Initialize and start the scheduler
    reminder = BirthdayReminder()
    reminder.start()
    
    # Keep the scheduler running
    try:
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        reminder.stop()
