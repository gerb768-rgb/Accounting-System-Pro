# زر عرض الرسم البياني للمدير
if user_role == "مدير":
    buttons.append(ft.ElevatedButton("عرض رسوم المبيعات", on_click=lambda _: graphics.generate_sales_chart(data)))
    buttons.append(ft.ElevatedButton("طباعة الفاتورة", on_click=lambda _: printer.print_invoice(invoice_id)))
  
