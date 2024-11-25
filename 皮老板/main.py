def getFrequency(text:str):
    # 创建一个空列表 freq，用于存储每个字母的出现次数
    fre = []

    # 使用 for 循环遍历从 0 到 25 的整数（因为英文字母表有 26 个字母，从 'a' 到 'z'）
    for i in range(26):
        # 在 freq 列表中添加 26 个 0，设置每个字母出现的次数为 0
        fre.append(0)

    # 遍历输入文本 text 中的每个字符，使用 .lower() 方法将文本字符串转换为小写(不区分大小写)
    for c in text.lower():
        # 检查字符 c 是否是 'a' 到 'z' 之间的字母
        if 'a'<= c <='z':
            # 计算字符 c 在字母表中的位置
            # ord('a') 得到 'a' 的 ASCII 值，然后从 c 的 ASCII 值中减去 'a' 的 ASCII 值
            pos = ord(c) - ord('a')
            fre[pos] += 1   # 将 freq 列表中对应位置 pos 的计数加 1
    return fre

print(getFrequency('hello world'))
