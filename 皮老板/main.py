# 导入了 Python 的 os 模块，该模块提供了对文件和目录的操作的功能
import os
inputPath = input('请输入待搜索的路径：')
pattern = input('请输入关键字：')

'''
使用 os.walk() 函数来遍历 inputPath 指定的目录及其所有子目录
os.walk() 生成一个三元组 (dirpath, dirnames, filenames)
其中 dirpath 是当前遍历到的目录路径，dirnames 是该目录下所有子目录的列表，filenames 是该目录下所有非目录文件的列表
'''
for dirpath,dirnames,filenames in os.walk(inputPath):
    # 遍历当前目录下的所有文件名
    for f in filenames:
        # 检查当前文件名 f 是否包含之前输入的关键字 pattern
        # 如果文件名中包含这个关键字，那么条件判断为真
        if pattern in f:
            # 打印出包含关键字的文件的完整路径
            print(f'{inputPath}/{f}')
