import xlrd
s=xlrd.open_workbook('students.py')

sh = s.sheet_by_index(0)
cell=sh.cell(0,0)
print cell
