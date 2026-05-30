import flet as ft
import main

def main_app(page: ft.Page):
    # حالة المستخدم (يمكن تغييرها بعد تسجيل الدخول)
    user_role = "مدير"  # أو "موظف" بناءً على نظام تسجيل الدخول

    def show_dashboard():
        # أزرار الموظف (الأساسية)
        buttons = [
            ft.ElevatedButton("إدخال فاتورة جديدة", icon=ft.icons.ADD),
            ft.ElevatedButton("فحص المخزون", on_click=lambda _: main.check_inventory())
        ]
        
        # أزرار المدير (الإضافية)
        if user_role == "مدير":
            buttons.extend([
                ft.ElevatedButton("تقرير المبيعات الشامل", icon=ft.icons.REPORTS, on_click=lambda _: main.generate_report()),
                ft.ElevatedButton("قفل فاتورة", icon=ft.icons.LOCK),
                ft.ElevatedButton("إدارة المستخدمين", icon=ft.icons.PERSON_ADD)
            ])
            
        page.add(ft.Column(buttons))

    page.add(ft.Text(f"لوحة تحكم: {user_role}", size=25, weight="bold"))
    show_dashboard()

ft.app(target=main_app)
