
from config import CURRENCY_ALERT_THRESHOLDS

def check_thresholds(rates):
    alerts = []
    for currency, rate in rates.items():
        if currency in CURRENCY_ALERT_THRESHOLDS:
            min_val, max_val = CURRENCY_ALERT_THRESHOLDS[currency]
            if min_val is not None and rate < min_val:
                alerts.append(f"⚠️ Alert: {currency} rate {rate} is below minimum threshold {min_val}.")
            if max_val is not None and rate > max_val:
                alerts.append(f"⚠️ Alert: {currency} rate {rate} is above maximum threshold {max_val}.")
    return alerts