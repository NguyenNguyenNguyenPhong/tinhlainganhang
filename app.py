from flask import Flask, render_template_string
import ast

app = Flask(__name__)

# Đọc dữ liệu từ file result.txt
def read_data_from_file():
    with open("D:/Project/scapyFinanal/cafef/cafef/spiders/result.txt", "r", encoding="utf-8") as file:
        data = file.read()
    return data

# Chuyển đổi dữ liệu từ chuỗi JSON sang Python
def parse_data(data):
    data_list = ast.literal_eval(data)
    return data_list

# Route để hiển thị dữ liệu dưới dạng bảng
@app.route("/")
def display_table():
    data = read_data_from_file()
    data_list = parse_data(data)
    headers = data_list[0]
    rows = data_list[1]
    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Dữ liệu lãi suất ngân hàng</title>
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }
                th, td {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }
                th {
                    background-color: #f2f2f2;
                }
            </style>
        </head>
        <body>
            <h1>Dữ liệu lãi suất ngân hàng</h1>
            <table>
                <thead>
                    <tr>
                        {% for header in headers %}
                        <th>{{ header }}</th>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody>
                    {% for row in rows %}
                    <tr>
                        {% for item in row %}
                        <td>{{ item }}</td>
                        {% endfor %}
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </body>
        </html>
        """,
        headers=headers,
        rows=rows
    )

if __name__ == "__main__":
    app.run(debug=True)
