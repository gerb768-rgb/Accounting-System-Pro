import main

# كلمة مرور المدير (يمكنك تغييرها لاحقاً)
ADMIN_PASSWORD = "123"

def login():
    password = input("أدخل كلمة مرور المدير: ")
    if password == ADMIN_PASSWORD:
        print("تم تسجيل الدخول بنجاح.")
        show_menu()
    else:
        print("كلمة مرور خاطئة! إغلاق النظام.")

def show_menu():
    # ... (بقية كود القائمة كما هو)
