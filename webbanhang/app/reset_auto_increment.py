from django.db import connection
from app.models import Payment_VNPay

# Xác định tên bảng của mô hình Payment_VNPay
table_name = Payment_VNPay._meta.db_table

# Thực hiện truy vấn SQL để đặt lại trường tự tăng
with connection.cursor() as cursor:
    cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")
