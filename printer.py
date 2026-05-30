import os
# إرسال الفاتورة للطابعة (بعد تحويلها لملف PDF)
def print_invoice(invoice_id):
    os.system(f"print /d:PrinterName invoice_{invoice_id}.pdf")
    print("تم إرسال الفاتورة للطابعة.")
