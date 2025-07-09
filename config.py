
# config.py
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env
load_dotenv(dotenv_path=Path(".") / ".env")

# Enable or disable email sending
SEND_EMAIL = True

# Filtered list of currencies (e.g., USD, EUR, BTC, ETH). If empty, all will be included.
FILTER_CURRENCIES = ["USD", "EUR", "BTC", "ETH"]

# Email settings
EMAIL_SENDER = os.getenv("EMAIL_USERNAME")
EMAIL_RECEIVER = "fariddivanpour@gmail.com"
EMAIL_SUBJECT = "Latest Filtered Currency Rates"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# Thresholds for alerting: currency_code -> (min_value, max_value)
CURRENCY_ALERT_THRESHOLDS = {
    "BTC": (None, 0.00002),    # هشدار اگر BTC بیشتر از 0.00002 شد
    "USD": (1.1, 1.3),         # هشدار اگر USD کمتر از 1.1 یا بیشتر از 1.3 شد
    "EUR": (0.9, 1.1),         # هشدار اگر EUR کمتر از 0.9 یا بیشتر از 1.1 شد
    # بقیه ارزها ...
}
