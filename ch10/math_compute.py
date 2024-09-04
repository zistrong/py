import math
def circleArea(r):
    """
    求元的面积
    @param r 半径
    """
    if r < 0:
        return 0
     
    return sectorArea(r, 355/113)


def sectorArea(r, radian):
    """
    扇形的面积
    @param r 半径
    @param radian 弧度
    """
    if radian<0:
        return 0
    if radian > 2*math.pi:
        return 0
    return r**2 * radian / 2 

def circumference(r):
    """圆周长"""
    if r<0:
        return 0
    return r * math.pi * 2

def lineFunction(gradient:float, point: tuple):
    """
    求直线方程
    @param gradient 斜率
    @param point 经过的点
    """
    A = gradient
    B = -1
    C = point[1] - gradient * point[0]
    if A > 0 :
        return (A, B, C) 
    else:
        return(-A, -B, -C)
def lineFunction(*args):
    p1 = args[0]
    p2 = args[1]
    if p1 == p2:
        return None
    if (p2[0]) == (p1[0]):
        return(1, 0, p1[0])
    gradient = ((p2[1])-(p1[1]))*1.0 / ((p2[0])-(p1[0]))
    return lineFunction(gradient = gradient, point=p1)


