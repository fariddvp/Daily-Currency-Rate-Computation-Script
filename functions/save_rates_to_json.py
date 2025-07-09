
import json
from datetime import datetime

def save_rates_to_json(rates, filename=None):
    date_str = datetime.now().strftime("%Y-%m-%d")
    data = {
        "date": date_str,
        "rates": rates
    }
    if filename is None:
        filename = f"rates_{date_str}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
