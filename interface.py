def show_menu(user_role):
    print(f"\n--- قائمة النظام ({user_role}) ---")
    if user_role == "مدير":
        print("1. فحص المخزون | 2. التقارير | 3. حذف فاتورة")
    else:
        print("1. إدخال فاتورة | 2. فحص المخزون")
