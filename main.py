def search_invoice(invoice_id):
    conn = sqlite3.connect('accounting_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM invoices WHERE id = ?", (invoice_id,))
    data = cursor.fetchone()
    if data:
        print(f"تفاصيل الفاتورة: {data}")
    else:
        print("الفاتورة غير موجودة.")
    conn.close()
