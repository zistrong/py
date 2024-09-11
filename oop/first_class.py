class FirstClass():
    def __init__(self, name) -> None:#构造函数
        self.name = name
    def __add__(self, other):#钩子方法， 重载+运算符
        return FirstClass(self.name + other.name)
    def setName(self, name):
        self.name = name
    def __test():
        pass
    
    def __str__(self) -> str:#打印， 转换成str，像Java中的toString()方法
        return self.name
    
if __name__ == '__main__':

    first = FirstClass('zhang')
    first1 = FirstClass('zi')
    print(first+first1)
    print(    round(float('5.6264'),2))


