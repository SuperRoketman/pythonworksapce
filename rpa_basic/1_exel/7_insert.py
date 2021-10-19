from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8번째 줄이 비워짐
# ws.insert_rows(8, 5) # 8번째 줄 위치에 5줄을 추가
# wb.save("sample_insert_row.xlsx")

# ws.insert_cols(2) # 2번째 열(B)이 비워짐
ws.insert_cols(2, 3) # 2번째 열(B)로부터 3열 추가

wb.save("sample_insert_cols.xlsx")