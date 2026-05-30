import flet as ft
import main 
import graphics 
import printer

def main_app(page: ft.Page):
    page.title = "نظام المحاسبة Pro - عمر يوسف البطحاني"
    user_role = "مدير" 

    def build_ui():
        page.add(ft.Text(f"لوحة تحكم النظام - المستخدم: {user_role}", size=20, weight="bold"))
        
        # الأزرار الأساسية
        page.add(
            ft.ElevatedButton("إدخال فاتورة جديدة", icon=ft.icons.ADD),
            ft.ElevatedButton("تقرير المخزون", on_click=lambda _: main.check_inventory()),
        )
        
        # صلاحيات المدير
        if user_role == "مدير":
            page.add(
                ft.Divider(),
                ft.ElevatedButton("عرض رسوم المبيعات", icon=ft.icons.BAR_CHART, on_click=lambda _: graphics.generate_sales_chart([])),
                ft.ElevatedButton("طباعة الفاتورة", icon=ft.icons.PRINT, on_click=lambda _: printer.print_invoice(1)),
                ft.ElevatedButton("حساب الضريبة (VAT 15%)", icon=ft.icons.CALCULATE, on_click=lambda _: print(main.calculate_invoice(1000))),
            )
        
        # الحقوق
        page.add(
            ft.Divider(),
            ft.Text("نظام محاسبي مطور بواسطة: عمر يوسف البطحاني", size=14, weight="bold", color="blue"),
            ft.Text("© جميع الحقوق محفوظة 2026", size=12, color="grey")
        )

    build_ui()

ft.app(target=main_app)
