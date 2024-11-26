def getFrequency(text:str):
    # 创建了一个空的字典 fre，用于存储每个字母的出现频率
    fre = {}

    # 使用 for 循环，遍历 text 字符串中的每个字符
    # 计数时不区分大小写, 使用 text.lower() 将所有的字符都被转换为小写，
    for c in text.lower():
        # 检查当前字符 c 是否是在 'a' 到 'z' 之间
        if 'a'<= c <='z':
            # 如果字符 c 已经在 fre 字典中，次数加 1
            if c in fre:
                fre[c] += 1
            # 如果字符 c 不在 fre 字典中，这意味着它是第一次出现，设置初始值为 1
            else:
                fre[c] = 1
    return fre

print(getFrequency('Tom likes to eat apples'))
