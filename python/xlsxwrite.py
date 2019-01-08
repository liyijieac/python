#xlsxwriter 模块的使用

import xlsxwriter
 
workbook = xlsxwriter.Workbook('new_excel.xlsx')
 
worksheet = workbook.add_worksheet('sheet1')
 
headings = ['Number','testA','testB']
 
data = [
    ['2017-9-1','2017-9-2','2017-9-3','2017-9-4','2017-9-5','2017-9-6'],
    [10,40,50,20,10,50],
    [30,60,70,50,40,30],
]
 
worksheet.write_row('A1',headings)
 
worksheet.write_column('A2',data[0])
worksheet.write_column('B2',data[1])
worksheet.write_column('C2',data[2])
 
 
workbook.close()  