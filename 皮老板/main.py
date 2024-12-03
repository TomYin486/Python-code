import math
# 导入 math 模块，可以使用数学常量和函数，如 pi(π)

'''
先定义了三个类：Point、Circle 和 Vector(点、圆、向量)，可以实现计算面积和周长、改变圆的大小和位置等
最后创建了一个 Circle 类的实例 s1，对其进行一些测试(如打印面积，周长，圆心位置等)
'''

# 定义一个 Point 类，用于表示二维空间中的点
class Point:
    # 初始化方法，设置点的 x 和 y 坐标
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # 获取点的 x 坐标
    def getX(self):
        return self._x

    # 获取点的 y 坐标
    def getY(self):
        return self._y

    def getCooedinate(self):
        return self._x, self._y

# 定义一个 Circle 类，用于表示二维空间中的圆
class Circle:
    # 初始化方法，设置圆的半径和圆心（使用 Point 类的实例）
    def __init__(self, radius: float, center: Point):
        self._radius = radius
        self._center = center

    def getCenterLocation(self):
        return (self._center)
        # 返回圆心的位置（返回 Point 类的实例）

    def getRadius(self):
        return self._radius
        # 返回圆的半径

    def getArea(self):
        return self._radius * self._radius * math.pi
        # 计算并返回圆的面积，公式为 πr²

    def getCircumference(self):
        return math.pi * self._radius * 2
        # 计算并返回圆的周长，公式为 2πr

    def enlarge(self, n):
        self._radius *= n
        # 将圆的半径扩大 n 倍

    def shrink(self, n):
        self._radius /= n
        # 将圆的半径缩小 n 倍

    def move(self, vector):
        x = self._center.getX() + vector.getX()
        y = self._center.getY() + vector.getY()
        newCenter = Point(x, y)
        self._center = newCenter
        # 将圆按照给定的向量移动，向量是一个 Vector 类的实例

# 定义一个 Vector 类，用于表示二维空间中的向量
class Vector:
    # 初始化方法，设置向量的 x 和 y 分量，并计算向量的长度
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._length = (x ** 2 + y ** 2) ** 0.5

    def getX(self):
        return self._x
        # 获取向量的 x 分量

    def getY(self):
        return self._y
        # 获取向量的 y 分量

# 创建一个 Circle 类的实例，半径为 2，圆心位于点(2,3)
s1 = Circle(3,Point(2,3))
# 打印圆 s1 的面积
print(s1.getArea())
# 打印圆 s1 的周长
print(s1.getCircumference())

# 调用 enlarge() 方法将圆 s1 的半径扩大 3 倍
s1.enlarge(3)
# 打印扩大后的圆 s1 的面积
print(s1.getArea())
# 打印扩大后的圆 s1 的周长
print(s1.getCircumference())

# 调用 shrink() 方法将圆 s1 的半径缩小 10 倍
s1.shrink(10)
# 打印缩小后的圆 s1 的面积
print(s1.getArea())
# 打印缩小后的圆 s1 的周长
print(s1.getCircumference())

# 打印圆 s1 的圆心位置
print(s1.getCenterLocation().getCooedinate())
# 或者直接访问 x 和 y 属性
# print((s1.getCenterLocation().getX(), s1.getCenterLocation().getY()))


# 创建一个 Vector 类的实例，表示向量(2,9)，然后调用 move() 方法将圆 s1 按照这个向量移动
s1.move(Vector(2,9))
# 打印移动后的圆 s1 的圆心位置
print(s1.getCenterLocation().getCooedinate())
# 或者直接访问 x 和 y 属性
# print((s1.getCenterLocation().getX(), s1.getCenterLocation().getY()))
