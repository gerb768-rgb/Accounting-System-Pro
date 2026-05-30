import sqlite3

def init_db():
    conn = sqlite3.connect('accounting_system.db')
    cursor = conn.cursor()

    # 1. جدول المستخدمين (للصلاحيات)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY, username TEXT, role TEXT)''')

    # 2. جدول المنتجات (مع حد الطلب للتنبيه)
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory 
                      (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, min_limit INTEGER)''')

    # 3. جدول الفواتير (مع حالة القفل)
    cursor.execute('''CREATE TABLE IF NOT EXISTS invoices 
                      (id INTEGER PRIMARY KEY, client_name TEXT, total REAL, status TEXT)''')

    conn.commit()
    conn.close()
    print("تم بناء قاعدة البيانات وجداول النظام بنجاح!")

if __name__ == "__main__":
    init_db()
