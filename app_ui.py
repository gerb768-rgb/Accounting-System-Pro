import flet as ft
import main     # المنطق الأساسي
import graphics # كود الرسوم البيانية
import printer  # كود الطباعة

def main_app(page: ft.Page):
    # هنا تضع كود الواجهة والداش بورد الذي قمنا بتصميمه سابقاً
    # تأكد من استدعاء الوظائف من الملفات الأخرى عند ضغط الأزرار
    # مثال: 
    # ft.ElevatedButton("طباعة", on_click=lambda _: printer.print_invoice(id))
    # ft.ElevatedButton("رسوم بيانية", on_click=lambda _: graphics.generate_sales_chart(data))
    
    page.update()

ft.app(target=main_app)
