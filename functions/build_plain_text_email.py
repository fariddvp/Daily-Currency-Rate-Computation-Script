
def build_plain_text_email(rates):
    lines = ["🔹 Selected Currency Rates:\n"]
    for currency, rate in sorted(rates.items()):
        lines.append(f"{currency}: {rate}")
    return "\n".join(lines)