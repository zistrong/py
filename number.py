import math
import decimal
import sys
import os
import pickle
import json

e = math.e

print(e)


com = 4+6j

print(com)

print(math.sin(e))

print(0b1010101+0O13+0x123f)

print(oct(83))
print(int(0o123))

print(complex(3,4)+6J)

print(pow(2.4,3))

print(math.log(e))

flag = -1

pi = 0

r = 1


print(r <0 or not flag == -1)

print(5/3.0,9)




decimal.getcontext().prec=2

big = decimal.Decimal("0.456")
print(big)


x  = set(['abc','fff'])
x.add('fsfd')
y = set("bcde")

print(x | y)

print(dir(x))

print(dir([]))

y = {x // 2 for x in {1,2,3}}

print(y)

b = True
print(b is True)


b = 7

if (b):
    c = 4
else:
    c = 'c'

print(c)


a = 5
b = 7

a,b=b,a
print(a, b)

print(sys.getrefcount(5))

shiju = '黄河远上白云间'

print(len(shiju))

c = 'cba'
#c = "C"


print(dir(c))

for i in c:
    print(i)


print(sys.argv)



def handleString(string):
    """处理字符串"""
    return string[1:]


print(handleString(string="0abc"))
name = 'zhang'

print("your name: {0}".format(name))





dic = {'k': 'abc', 'k1':'kk'}

print(dic.get("k",'value'))



print(list(dic.keys()))



print(dict.fromkeys(['a', 'b'], 6))

d = [v for v in dic.keys()]

print(d)

#元组

meta1 = (1,2,3,4)

print(meta1)
print(meta1[2])
print(len(meta1))

print("打印元组")
for m in meta1:
    print(m)


meta2 =3,4,56

print(meta1[1:3])

print(len(meta2))

print(sum(meta1))


#文件操作

#读写操作，追加
output = open("E:/tech/python/py/a.txt","a+")
output.readline()
output.writelines('黄河远上白云间\n')
output.flush()
output.close()


input = open("E:/tech/python/py/a.txt","r")

line = input.readline()

print(line)

input.close()

for line in open("E:/tech/python/py/a.txt","r"):
    print(line, end='')


# output = open("E:/tech/python/py/b.txt","a+")
# output.write(json.dumps({'a':'zag','b':5})+'\n')
# output.flush()
# output.close()

# for line in open("E:/tech/python/py/b.txt","r"):
#     print(eval(line).get('a'), end='')


pickle.dump({'name':'zhang', 'age' : 35}, open("E:/tech/python/py/c.txt", 'wb'))


eval('print("abc")')


with open("E:/tech/python/py/c.txt", 'rb') as myfile:
    u = pickle.load(myfile)
    print(u['name'])

sys.stdout.write('adfs\n')




obj = None

print(obj is None)


if(None):
    print(True)
else:
    print(False)

print(type(type(type(line))))

class Employee():
    """Employee类"""
    def __init__(self) -> None:
        pass
    def setId(self, id) -> None:
        self.id = id
    def getId(self):
        return self.id
    
employee = Employee()
employee.setId(4)

print(employee.getId())

print(type(employee))

class Manager(Employee):
    """Manager类"""
    def __init__(self) -> None:
        super().__init__()


manager = Manager()

print(isinstance(employee, Manager))





