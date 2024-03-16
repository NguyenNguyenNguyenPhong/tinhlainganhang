from flask import Flask, jsonify

app = Flask(__name__)

# Đọc dữ liệu từ file result.txt và xử lý thành dữ liệu dạng list
def read_data_from_file():
    with open("D:/Project/scapyFinanal/cafef/cafef/spiders/result.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    header = eval(lines[0])  # Dòng đầu tiên là header
    data = [eval(line) for line in lines[1:]]  # Các dòng tiếp theo là dữ liệu
    return header, data

# Route để trả về dữ liệu dưới dạng JSON
@app.route("/api/data", methods=["GET"])
def get_data():
    header, data = read_data_from_file()
    result = {"data": data,"header": header}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
