from math import hypot


class Vector():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x,self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))


    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x * scalar,self.y * scalar)



"""
__repr__把一个对象用字符串形式表达出来以便辨认
__repr__和__str__的区别在于，后者是在str()函数中被使用，或是在用print函数打印一个对象时才被调用
"""
v1 = Vector(2,4)
print(v1) # Vector(2,4)

"""
__add__ 表示两个类变量的相加操作
__mul__ 表示类变量的算术乘法操作
"""

v2 = Vector(1,3)
print(v1 + v2) # Vector(3,7)

print(v1 * 3) # Vector(6,12)

"""
__bool__判定一个对象是真还是假，调用bool方法时会调用该函数
"""

print(bool(v1)) # True

"""
当然还有很多其他的特殊方法
"""




