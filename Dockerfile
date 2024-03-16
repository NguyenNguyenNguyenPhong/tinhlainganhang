# Sử dụng Python 3.11
FROM python:3.11

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép tất cả các tệp từ thư mục hiện tại vào thư mục /app trong container
COPY . /app

# Cài đặt các thư viện từ file requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng 5000 để Flask có thể lắng nghe yêu cầu
EXPOSE 5000

# Khởi chạy ứng dụng Flask
CMD ["python", "app.py"]
