import shutil
import datetime
import os

def create_backup():
    # اسم ملف النسخة الاحتياطية مع التاريخ
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{date_str}.db"
    
    # التأكد من وجود قاعدة البيانات قبل النسخ
    if os.path.exists('accounting_system.db'):
        shutil.copy('accounting_system.db', backup_filename)
        print(f"تم إنشاء نسخة احتياطية بنجاح: {backup_filename}")
    else:
        print("خطأ: ملف قاعدة البيانات غير موجود.")
