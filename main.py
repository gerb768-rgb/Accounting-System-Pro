def process_sale(product_name, quantity_sold, client_name):
    conn = sqlite3.connect('accounting_system.db')
    cursor = conn.cursor()
    
    # 1. التأكد من توفر المخزون
    cursor.execute("SELECT id, quantity, min_limit FROM inventory WHERE name = ?", (product_name,))
    product = cursor.fetchone()
    
    if product and product[1] >= quantity_sold:
        # 2. خصم الكمية من المخزون
        new_qty = product[1] - quantity_sold
        cursor.execute("UPDATE inventory SET quantity = ? WHERE name = ?", (new_qty, product_name))
        
        # 3. تسجيل الفاتورة
        cursor.execute("INSERT INTO invoices (client_name, total, status) VALUES (?, ?, ?)", 
                       (client_name, 0, 'Open')) # الإجمالي سيتم حسابه لاحقاً
        
        conn.commit()
        print("تمت عملية البيع وخصم المخزون بنجاح.")
        
        # 4. التنبيه إذا وصل المخزون لمستوى حرج
        if new_qty < product[2]:
            print("⚠️ تنبيه: مستوى المخزون أصبح حرجاً (🔴 أحمر)!")
    else:
        print("خطأ: الكمية غير متوفرة أو المنتج غير موجود.")
    conn.close()
