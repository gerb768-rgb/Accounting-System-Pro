import main  # استدعاء الدوال التي كتبناها سابقاً

def show_menu():
    print("\n--- نظام المحاسبة المركزي ---")
    print("1. فحص حالة المخزون")
    print("2. قفل فاتورة")
    print("3. إجراء مرتجع")
    print("4. خروج")
    
    choice = input("اختر عملية: ")
    
    if choice == '1':
        main.check_inventory()
    elif choice == '2':
        inv_id = input("أدخل رقم الفاتورة للقفل: ")
        main.lock_invoice(inv_id)
    elif choice == '3':
        inv_id = input("أدخل رقم الفاتورة للمرتجع: ")
        amount = input("أدخل مبلغ المرتجع: ")
        main.process_return(inv_id, amount)
    elif choice == '4':
        exit()
    
    show_menu() # العودة للقائمة

if __name__ == "__main__":
    show_menu()
