
import csv
from datetime import datetime

def save_rates_to_csv(rates, filename="currency_rates.csv"):
    date_str = datetime.now().strftime("%Y-%m-%d")
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header if file is empty
        if file.tell() == 0:
            writer.writerow(["date", "currency", "rate"])
        for currency, rate in rates.items():
            writer.writerow([date_str, currency, rate])
