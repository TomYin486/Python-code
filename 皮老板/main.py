def addString(stringList, string):
    """向列表中添加一个字符串，并返回更新后的列表"""
    stringList.append(string)
    return stringList


def deleteString(stringList, string):
    """从列表中移除所有指定的字符串"""
    assert string in stringList, "String not found in the list."
    while string in stringList:
        stringList.remove(string)
    return stringList


def searchString(stringList, string):
    """在列表中搜索指定字符串，并返回所有位置"""
    assert string in stringList, "String not found in the list."
    positions = []
    index = 0
    for each in stringList:
        if each == string:
            positions.append(index)
        index += 1
    return positions


def replaceString(stringList, oldString, newString):
    """将列表中所有的旧字符串替换为新字符串"""
    assert oldString in stringList, "Old string not found in the list."
    for i in range(len(stringList)):
        if stringList[i] == oldString:
            stringList[i] = newString
    return stringList


def menu():
    """显示菜单选项"""
    print("1. Add String")
    print("2. Delete String")
    print("3. Search String")
    print("4. Replace String")
    print("0. Exit")


# 初始化列表
stringList = ["apple", "banana", "cherry", "apple"]
options = [0, 1, 2, 3, 4]
print("stringList:", stringList)

menu()  # 打印菜单
# 获取一个有效的输入(0, 1, 2, 3, 4)
option = int(input("Enter an option (0, 1, 2, 3, 4):"))
while option not in options:
    print("Error input, enter an option again!")
    option = int(input("Choose an option (0, 1, 2, 3, 4):"))

while option != 0:
    # 添加字符串
    if option == 1:
        string = input("Enter string to add: ")
        stringList = addString(stringList, string)

    # 删除字符串
    elif option == 2:
        string = input("Enter string to delete: ")
        stringList = deleteString(stringList, string)

    # 搜索字符串
    elif option == 3:
        string = input("Enter string to search: ")
        result = searchString(stringList, string)
        if len(result):
            print("The position(s) of the string in the stringList is(are):", result)
        else:
            print("The string is not in the stringList")

    # 替换字符串
    elif option == 4:
        oldString = input("Enter old string: ")
        newString = input("Enter new string: ")
        stringList = replaceString(stringList, oldString, newString)

    print("stringList:", stringList)
    menu()

    # 再次获取一个有效的输入(0, 1, 2, 3, 4)
    option = int(input("Enter an option (0, 1, 2, 3, 4):"))
    while option not in options:
        print("Error input, enter an option again!")
        option = int(input("Enter an option (0, 1, 2, 3, 4):"))
print("exit")
