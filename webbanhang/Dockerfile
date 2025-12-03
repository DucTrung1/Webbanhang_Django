# Sử dụng Python 3.10
FROM python:3.10

# Thiết lập thư mục làm việc
WORKDIR /app

# --- PHẦN MỚI THÊM VÀO ---
# Cài đặt các công cụ hệ thống cần thiết để build mysqlclient
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
# -------------------------

# Copy requirements và cài đặt thư viện
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy toàn bộ code
COPY . .

# Mở port
EXPOSE 8000

# Chạy server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]