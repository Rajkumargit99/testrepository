import openpyxl

def read_excel_file(file_path, sheet_name, cell_name):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]
    cell = sheet[cell_name]
    print(cell.value)

read_excel_file("user_data.xlsx", "Sheet1", "D1")
print("-------------------------------------------------------------")

for i in range(1,6):
    read_excel_file("user_data.xlsx", "Sheet1", f"A{i}")
print("-------------------------------------------------------------")

def write_excel_file(file_path, sheet_name, cell_name, cell_value):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]
    cell = sheet[cell_name]
    cell.value = cell_value
    wb.save(file_path)
    print(cell.value)

write_excel_file("user_data.xlsx", "Sheet1", "b1","2021")
write_excel_file("user_data.xlsx", "Sheet1", "b2","2022")
write_excel_file("user_data.xlsx", "Sheet1", "b3","2023")
write_excel_file("user_data.xlsx", "Sheet1", "b4","2024")