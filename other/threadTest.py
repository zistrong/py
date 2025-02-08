import threading  
import time  
import math
import secrets
  
def print_numbers():  
    for i in range(5):  
        time.sleep(1)  # 模拟耗时操作  
        print(i)  
  
def print_letters():  
    for i in 'abcde234wefsdfsdf':  
        time.sleep(1)  # 模拟耗时操作  
        print(i)  
  
def startThread():
    # 创建线程  
    t1 = threading.Thread(target=print_numbers)  
    t2 = threading.Thread(target=print_letters)  
    # 启动线程  
    t1.start()  
    t2.start()  
    t2.join()  
    t1.join()
    # 等待线程完成  
    print("Done!")

for i in range(0,9,2):
    print(i)

