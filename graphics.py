import matplotlib.pyplot as plt

def generate_sales_chart(sales_data):
    # sales_data عبارة عن قائمة بالتواريخ وقيم المبيعات
    dates = [d[0] for d in sales_data]
    values = [d[1] for d in sales_data]
    
    plt.plot(dates, values)
    plt.title("تقرير المبيعات الشهري")
    plt.xlabel("التاريخ")
    plt.ylabel("الإجمالي")
    plt.show()
