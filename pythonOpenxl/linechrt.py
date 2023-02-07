from openpyxl.chart import LineChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sales_data=[
    ["product","sales","year"],
    [1,1000,2001],
    [2,2000,2002],
    [3,3000,2003],
    [4,4000,2004],
    [5,5000,2005],
    [6,6000,2006],
    [7,7000,2007],
            ]
for i in sales_data:
    sheet.append(i)

chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")

wb.save("..//data//line.xlsx")

