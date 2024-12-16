

import time
def fibonacci1(n):
    if n in [1,2]:
        return 1
    else:
        return fibonacci1(n-2) + fibonacci1(n-1)

# ret1 = fibonacci(8)
# print(ret1)

# def fibonacci1(n):
#     if n in [1,2]:
#         return 1
#     else:
#         a, b = 0, 1
#         for i in range(2, n + 1):
#
#             a, b = b, a + b
#         return b

def fibonacci2(n):
    if n in [1,2]:
        return 1
    nums = [1,1]
    for i in range(2,n):
        nextNum = nums[i - 1] + nums[i - 2]
        nums.append(nextNum)
    return nums[n - 1]

def fibonacci3(n):
    if n in [1,2]:
        return 1
    a = 0
    b = 0
    c = 1
    while n != 1:
        a = b
        b = c
        c = a + b
        n -= 1
    return c

#print(fibonacci1(50))

# print(fibonacci2(50))
# print(fibonacci3(50))
# def mearsure(function,param,n):
#     start = time.time()
#     for _ in range(n):
#         function(param)
#     end = time.time()
#     return (end - start)*100
#
# print(mearsure(fibonacci1,25,15))
# print(mearsure(fibonacci2,25,15))
# print(mearsure(fibonacci3,25,15))

class Book:
    def __init__(self,title):
        self._title= title
# book1 = Book('12')
# print([book1])

try:
    with open()





