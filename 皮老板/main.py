def rotateString(s,goal):
    # 检查字符串 s 和 goal 的长度是否相等。如果长度不同，那么 s 不可能通过旋转变成 goal
    if len(s) != len(goal):
        return False
    else:
        # 这个 (s+s) 包含了 s 的两次重复，从而覆盖了 s 的所有可能的旋转
        # 如果 goal 是 s 的一个旋转，那么它也是 (s+s) 的子串
        if goal in (s+s):
            return True
        else:
            return False

# 可以简化
# def rotateString(s,goal):
#     if len(s) != len(goal):
#         return False
#     return goal in (s+s)

print(rotateString('cab','abc'))
