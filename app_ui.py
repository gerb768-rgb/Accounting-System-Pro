import flet as ft
import main     # استيراد منطق النظام
import graphics # استيراد الرسوم البيانية
import printer  # استيراد وظائف الطباعة

def main_app(page: ft.Page):
    page.title = "نظام المحاسبة المحترف"
    
    # تعريف الأدوار (يمكنك ربطها بنظام تسجيل دخول لاحقاً)
    user_role = "مدير" 

    def build_ui():
        # الأزرار الأساسية للموظف والمدير
        page.add(ft.Text(f"لوحة التحكم - المستخدم: {user_role}", size=20, weight="bold"))
        
        # أزرار النظام
        page.add(
            ft.ElevatedButton("إدخال فاتورة جديدة", icon=ft.icons.ADD),
            ft.ElevatedButton("عرض تقرير المخزون", on_click=lambda _: main.check_inventory()),
        )
        
        # صلاحيات المدير الإضافية
        if user_role == "مدير":
            page.add(
                ft.Divider(),
                ft.Text("أدوات المدير:", weight="bold"),
                ft.ElevatedButton("عرض رسوم المبيعات", icon=ft.icons.BAR_CHART, on_click=lambda _: graphics.generate_sales_chart([])),
                ft.ElevatedButton("طباعة آخر فاتورة", icon=ft.icons.PRINT, on_click=lambda _: printer.print_invoice(1)),
                ft.ElevatedButton("إدارة النسخ الاحتياطي", icon=ft.icons.BACKUP)
            )

    build_ui()

ft.app(target=main_app)
