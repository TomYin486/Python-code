# 该函数接受两个参数：words（列表）和 s（字符串）
def countPrefixes(words:list,s:str):
    count = 0
    # 遍历 words 列表中的每个字符串 word
    for word in words:
        # 使用 startswith 方法检查字符串 s 是否以 word 作为前缀开始
        # 如果 word 是 s 的前缀，startswith 方法返回 True；如果不是，则返回 False
        if s.startswith(word):
            count += 1
    return count

print(countPrefixes(['a','abc','aa'],'abc'))
