from flask import Flask, jsonify

app = Flask(__name__)

# Đọc dữ liệu từ file result.txt và xử lý thành dữ liệu dạng list
def read_data_from_file():
    # Đọc dữ liệu từ tệp tin
    file_path = "D:\Project\scapyFinanal\cafef\cafef\spiders\\result.txt"
    with open(file_path, 'r', encoding='utf-8') as file:
        data_txt = file.read()

    # Tách dữ liệu thành các dòng
    lines = data_txt.split('], ')

    # Tạo một danh sách hai chiều từ các giá trị trong mỗi ô vuông
    data_list = []
    for line in lines:
        row_data = line.strip('[]').split(', ')
        # Loại bỏ dấu ngoặc kép từ các giá trị
        row_data = [value.replace('"', '') for value in row_data]
        data_list.append(row_data)

    # In kết quả
    header = data_list[0]
    data = data_list[1:]
    return header,data

# Route để trả về dữ liệu dưới dạng JSON
@app.route("/api/data", methods=["GET"])
def get_data():
    header, data = read_data_from_file()
    result = {"data": data, "header": header}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
