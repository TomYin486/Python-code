# 接受两个参数：freq（列表，用于表示字母及出现次数）和 letter（字符，表示要添加到频率列表中的字母）
def addLetter(freq, letter):
    i = 0

    # 使用 while 循环来遍历 freq 列表，直到找到匹配的字母或者到达列表的末尾
    '''
    在 freq 列表中搜索字母 letter，如果找到了，就跳出循环
    如果遍历完整个列表都没有找到，i 将等于 len(freq)，表示 letter 不在列表中，需要被添加到列表中
    如果找到了，就更新该字母的计数
    '''
    while i != len(freq) and freq[i][0] != letter:
        i = i + 1
    assert i == len(freq) or freq[i][0] == letter
    if i == len(freq):
        freq.append([letter, 1])
    else:
        freq[i][1] += 1
    return freq

def getFrequency2(text):
    # 初始化一个空列表 freq，用于存储字母及其出现频率
    freq = []

    # 遍历 text 字符串的每个字符，并将字符串转换为小写(不区分大小写)
    for c in text.lower():
        # 检查当前字符 c 是否是在 'a' 到 'z' 的范围内
        if 'a' <= c <= 'z':
            # 如果是字母，调用addLetter函数，将 c 添加到 freq 列表中，并更新其计数
            freq = addLetter(freq, c)
    return freq

print(getFrequency2('abcaabcdhf'))
