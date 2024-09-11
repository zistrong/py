from first_class import FirstClass
class SecondClass(FirstClass):
    def __init__(self) -> None:
        super().__init__('zhangzistrong')#使用super()方法
        #FirstClass.__init__(self,'zhangzistrong') 使用对象名称方式， 需要手动传入self对象
    def __test():
        pass
if __name__ == '__main__':
    print(getattr(SecondClass(), 'name'))

