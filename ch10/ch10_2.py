
import math

def isPrime(num):
    """
    判断一个数是否是素数,<p>
    如果是2， 直接返回True<p>
    如果是偶数， 直接返回False<p>
    求方根, 从3开始循环， 检查是否有奇数被整除
    """
    n = 2
    if num == n:
        return True
    
    if not num % n:
        return False
    n = 3
    sqrt = math.floor(math.sqrt(num))
    while n <= sqrt:
        if not num % n:
            return False
        n += 2
    return True


print(isPrime(97))


def gcd(a, b):
    """求最大公约数,使用辗转相除"""
    if a < b: a,b = b,a
    while a % b: b,a = a % b,b
    return b
