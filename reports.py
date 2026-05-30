import sqlite3
import csv

def generate_report():
    conn = sqlite3.connect('accounting_system.db')
    cursor = conn.cursor()
    
    # سحب كافة البيانات المطلوبة للتقرير
    cursor.execute("SELECT * FROM invoices")
    invoices = cursor.fetchall()
    
    # كتابة البيانات في ملف CSV
    with open('report.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["رقم الفاتورة", "اسم العميل", "الإجمالي", "الحالة"])
        writer.writerows(invoices)
        
    conn.close()
    print("تم توليد التقرير بنجاح باسم 'report.csv'. يمكنك الآن رفعه أو استخدامه.")
