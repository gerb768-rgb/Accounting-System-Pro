import sqlite3

# دالة لقفل الفاتورة (لا يمكن تعديلها بعد هذا)
def lock_invoice(invoice_id):
    conn = sqlite3.connect('accounting_system.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE invoices SET status = 'Locked' WHERE id = ?", (invoice_id,))
    conn.commit()
    conn.close()
    print(f"تم قفل الفاتورة رقم {invoice_id} بنجاح. لا يمكن تعديلها الآن.")

# دالة التنبيه بالمخزون (الأحمر والأخضر)
def check_inventory():
    conn = sqlite3.connect('accounting_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity, min_limit FROM inventory")
    products = cursor.fetchall()
    
    print("--- تقرير المخزون ---")
    for p in products:
        name, qty, limit = p
        status = "🟢 أخضر (متوفر)" if qty >= limit else "🔴 أحمر (نقص - يرجى الطلب)"
        print(f"المنتج: {name} | الكمية: {qty} | الحالة: {status}")
    conn.close()

# دالة معالجة المرتجعات (مع الحفاظ على سلامة الفاتورة)
def process_return(invoice_id, return_amount):
    conn = sqlite3.connect('accounting_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM invoices WHERE id = ?", (invoice_id,))
    status = cursor.fetchone()
    
    if status and status[0] == 'Locked':
        print(f"جاري معالجة المرتجع للفاتورة {invoice_id} بمبلغ {return_amount}...")
        # هنا يتم إضافة قيد المرتجع في قاعدة البيانات
    else:
        print("خطأ: لا يمكن إجراء مرتجع لفاتورة غير مقفلة!")
    conn.close()
