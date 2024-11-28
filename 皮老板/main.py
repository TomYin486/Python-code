# 导入 xlrd 模块，用于读取Excel文件（.xls和.xlsx）的 Python 库
import xlrd

'''
这个是 Excel 表中的数据
   0       1        2
0  姓名	   班级	    成绩
1  Alan1   202311	61
2  Alan2   202311	78
3  Alan3   202311	89
4  Alan4   202311	99
5  Alan5   202311	82
6  Alan6   202312	66
'''

# 1. 打开 xlsx 文件(使用 xlrd.open_workbook 函数打开位于指定路径的Excel文件)
xlsx = xlrd.open_workbook('d:/浏览器下载的/Jack/excell.xlsx')

# 2. 获取 0 号标签页. (当前只有一个标签页,即通过索引（0号，即第一个标签页）获取Excel文件中的工作表)
table = xlsx.sheet_by_index(0)

# 3. 获取总行数
nrows = table.nrows

# 4. 遍历数据
count = 0
total = 0
for i in range(1, nrows):
    # 使用 cell_value(row, col) 获取到指定坐标单元格的值
    # 使用 cell_value 方法获取当前行第 1 列的值(列数从 0 开始)
    classId = table.cell_value(i, 1)
    if classId == 202311:
        # 如果班级ID匹配，将当前行第 2 列(列数从 0 开始)的值加到 total 上
        total += table.cell_value(i, 2)
        count += 1
print(f'平均分: {total / count}')
