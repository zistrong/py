import random
import math

print(3.14149*3)

print(random.random())

print(math.e)


str = '0123456789'

print(str)

print(str[0:])
print(str[1:])
print(str[-2:])
print(str[-2:0])
print(str[3:5])
a = 6
b = 7
print(str[a:b])

test1 = '   abc kd l    '
print(test1.strip())

#定义类
class Employee:
    def __init__(self)->None:
        pass
    def __init__(self,id) -> None:
        self.id = id
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id



e = Employee(7)
e.setId(5)
print(e.getId())



