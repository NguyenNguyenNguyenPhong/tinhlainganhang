import requests
from bs4 import BeautifulSoup

url = "https://s.cafef.vn/lai-suat-ngan-hang.chn#data"
res = requests.get(url)
htmldiv = BeautifulSoup(res.content, 'html.parser')  # Specify parser
htmldiv.encoding = 'utf-8'
print(htmldiv)

tableData = htmldiv.find("tbody", {"id": "tb-interest-rate"})
cellHeaders = htmldiv.find("thead", {"id": "header-table-interest"})
jsonTitle = []
# jsonTitle.append("VCB_BaoCaoLuyKe_6_Thang")
jsonHeader = []

# Fix the cellHeaders checking for NoneType
if cellHeaders:
    cellHeader = cellHeaders.find("tr")  # Find the 'tr' tag within the thead
    for header in cellHeader.find_all("th", limit=8):  # limit to 8 columns
        jsonHeader.append(header.text.strip())

linesTable = tableData.find_all("tr")
jsonData = []

for lineTable in linesTable:
    cellTables = lineTable.find_all("td", limit=8)
    jsonData_line = []
    for cellTable in cellTables:
        jsonData_line.append(cellTable.text.strip())
    jsonData.append(jsonData_line)

jsonData.insert(0, jsonTitle)  # Insert jsonTitle without unpacking
jsonData.insert(1, [""] + jsonHeader)  # Insert an empty string as the first element

# Printing for testing
for data in jsonData:
    print(data)
