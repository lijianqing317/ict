import xlrd
data = xlrd.open_workbook('ljqdp.xlsx')
table_target = data.sheet_by_name('target')
print table_target.col_values(0)
classify = list(set(table_target.col_values(0)))
print classify
print classify.index(3.25)
dic = {}
for i in classify:
    dic[i] = classify.index(i)
list_target = []
for j in table_target.col_values(0):
    list_target.append(dic[j])
print list_target