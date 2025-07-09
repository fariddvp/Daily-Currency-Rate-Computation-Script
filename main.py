
import os
from dotenv import load_dotenv
from pathlib import Path

from functions.check_thresholds import check_thresholds
from functions.build_plain_text_email import build_plain_text_email
from functions.save_rates_to_csv import save_rates_to_csv
from functions.save_rates_to_json import save_rates_to_json
from functions.fetch_currency_rates import fetch_currency_rates
from functions.send_email import send_email
from config import SEND_EMAIL, FILTER_CURRENCIES

def main():
    # Load environment variables from .env file
    load_dotenv(dotenv_path=Path(".") / ".env")

    # Get API key and base URL from environment variables
    api_key = os.getenv("FIXER_API_KEY")
    base_url = os.getenv("BASE_URL")

    if not api_key or not base_url:
        raise ValueError("API key or BASE_URL is not set in the environment variables.")

    # Fetch currency rates from API
    response = fetch_currency_rates(api_key, base_url)

    # Check for success
    if not response.get("success", False):
        print(f"❌ Error fetching currency rates: {response.get('error', 'Unknown error')}")
        return

    # Extract and filter currency rates
    rates = response.get("rates", {})
    if not rates:
        print("⚠️ No currency rates available.")
        return

    filtered = {k: v for k, v in rates.items() if not FILTER_CURRENCIES or k in FILTER_CURRENCIES}

    # Save data to JSON and CSV files
    save_rates_to_json(filtered)
    save_rates_to_csv(filtered)

   # Build plain text email content
    alerts = check_thresholds(filtered)
    alert_message = "\n".join(alerts) if alerts else "No alerts."

    email_content = build_plain_text_email(filtered) + "\n\n" + alert_message

    print(email_content)



    if SEND_EMAIL:
        send_email(email_content)


if __name__ == "__main__":
    main()
