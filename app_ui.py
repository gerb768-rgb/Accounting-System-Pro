import flet as ft
import main  # سنستدعي دوالنا السابقة هنا

def main_app(page: ft.Page):
    page.title = "نظام المحاسبة المحترف"
    
    # حقل إدخال رقم الفاتورة
    invoice_input = ft.TextField(label="رقم الفاتورة للبحث")
    
    # دالة البحث عند الضغط على الزر
    def search_click(e):
        result = main.search_invoice(invoice_input.value)
        page.add(ft.Text(f"النتيجة: {result}"))

    # إضافة الأزرار للواجهة
    page.add(
        ft.Text("أهلاً بك في نظام الإدارة المالية", size=20),
        invoice_input,
        ft.ElevatedButton("بحث عن فاتورة", on_click=search_click),
        ft.ElevatedButton("عرض تقرير المخزون", on_click=lambda _: main.check_inventory())
    )

ft.app(target=main_app)
