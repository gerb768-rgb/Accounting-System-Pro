def calculate_invoice(amount):
    vat_rate = 0.15  # ضريبة 15%
    vat = amount * vat_rate
    total = amount + vat
    # تنسيق الأرقام بالجنيه السوداني
    return {
        "amount": f"{amount:,.2f} ج.س",
        "vat": f"{vat:,.2f} ج.س",
        "total": f"{total:,.2f} ج.س"
    }
