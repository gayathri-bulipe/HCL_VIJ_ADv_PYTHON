from openpyxl.chart import BarChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sales_data=[
    ["product_id","Online","Store"],
    [1,35,45],
    [2,67,78],
    [3,56,78],
    [4,55,78],
    [5,66,79],
    [6,45,66],
    [7,78,33],

]
for row in sales_data:
    sheet.append(row)

chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")

wb.save("..//data//chart.xlsx")



