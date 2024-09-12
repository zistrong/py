import sys
import string
import array
import statistics
import socket
def charAt(source: str, index: int):
    return source[index]

class MyException(Exception):
    pass

class YourException(Exception):
    pass

try:
    print(charAt('abcdef', 3))
    #print(charAt('abcdef', 6))
    raise MyException('xxxx')
except (MyException, YourException) as x:
    print('error!', x)
finally:
    print('clean')

print(string.capwords('ABCd张').title())

print(statistics.median([1,2,3,4,1,0])) #中位数

