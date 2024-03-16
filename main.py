import pandas as pd

file_path = r'D:\Project\scapyFinanal\cafef\cafef\spiders\result.txt'

# Đọc dữ liệu từ tệp tin
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

df = pd.DataFrame(data, columns=header)
print(df)
value = df.loc[0, 'Ngân hàng']
print(value)
# Lấy giá trị của cột 'Không kỳ hạn' tại dòng thứ 2
value = df['Không kỳ hạn'][2]
print(value)
# Lấy giá trị của cột thứ 2 tại dòng thứ 3
value = df.iloc[3, 2]
print(value)


