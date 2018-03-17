
import  openpyxl
wb=openpyxl.load_workbook("importweather.xlsx")
print(wb.get_sheet_names())

print(wb.active)
sheet=wb.active
