import sys
import math
import numpy as np
import decimal
import fractions
from sympy import *
import numpy as np  

input = "adventofcode/2023/input/day24.input"

MIN = 200000000000000
MAX = 400000000000000

def part1():
    """求方程的交点"""
    hailStones = []

    with open(input) as file:
        for l in file:
            line = l.strip().split('@')
            position = tuple(int(l) for l in line[0].split(','))
            velocity = tuple(int(l) for l in line[1].split(','))
            if withArea(position) or possibleInter(position, velocity):
                hailStones.append({'p': position, 'v': velocity})
        count = 0
        for i in range(len(hailStones)):
            for j in range(i, len(hailStones)):
                h1 = hailStones[i]
                h2 = hailStones[j]
                root = findRoots(h1, h2)
                if any(root):
                    if root[0]>=MIN and root[0]<=MAX and root[1]>=MIN and root[1]<=MAX and crossSinceNow(root, h1) and crossSinceNow(root, h2):
                        count+=1
        print(count) 


def findRoots(f1={'p':[], 'v':[]}, f2={'p':[], 'v':[]}) -> tuple: 
    """
        使用克莱姆法则求方程的根<p>
        v00 = f1['v'][0]<p>
        v01 = f1['v'][1]<p>
        x00 = f1['p'][0]<p>
        x01 = f1['p'][1]<p>

        A = f1['v'][1]/f1['v'][0]<p>
        B = -1<p>
        C=f1['v'][1]*f1['p'][0]/f1['v'][0]-f1['p'][1]<p>

        D = A2 - A1<p>
        D1 = C2-C1<p>
        D2=A1*C2-A2*C1<p>
        x = D1/D<p>
        y = D2/D<p>
        """
    A = np.array([[f1['v'][1]/f1['v'][0], -1],[f2['v'][1]/f2['v'][0], -1]])
    b = np.array([f1['v'][1]*f1['p'][0]/f1['v'][0]-f1['p'][1], f2['v'][1]*f2['p'][0]/f2['v'][0]-f2['p'][1]])
    if f1['v'][0]/f1['v'][1] == f2['v'][0]/f2['v'][1] :#斜率相同，直线平行，无解
        return ()
    else :
        return np.linalg.solve(A, b)

def compare(root, v, p):
    if v > 0 and root>p:
        return True
    if v < 0 and root<p:
        return True
    return False
    
def crossSinceNow(root= (), f={'p':[], 'v':[]})->bool:
    """判断是否在未来相交"""
    return compare(root[0], f['v'][0], f['p'][0]) and compare(root[1], f['v'][1], f['p'][1]) 



def withArea(position):
    """起点在区域内就可能相交"""
    return int(position[0])>=MIN and int(position[0])<=MAX and int(position[1])>=MIN and int(position[1])<=MAX

def possibleInter(position, velocity) :
    """判断两条直线是否可能相交"""
    if position[0]<=MIN and position[1]>=MAX: #左上
        if velocity[0]>0 and velocity[1]<0:
            return True
        else:
            return False
    if position[0]>=MAX and position[1]<=MIN:#右下
        if velocity[0]<0 and velocity[1]>0:
            return True
        else:
            return False
        
    if position[0]>=MIN and position[0]<=MAX and position[1]>MAX:#上
        if velocity[1]>0:
            return False
        else:
            return True
    if position[0]>=MIN and position[0]<=MAX and position[1]<MIN:#下
        if velocity[1]<0:
            return False
        else:
            return True
        
    if position[0]> MAX and position[1]>MAX:#右上
        if velocity[0]>0 and velocity[1]>0:
            return False
        else:
            return True
        
    if position[0]<MIN and position[1]<MIN:#左下
        if velocity[0]<0 and velocity[1]<0:
            return False
        else:
            return True

    if position[0]<=MIN and position[1]>=MIN and position[1]<MAX:#左
        if velocity[0]<0:
            return False
        else:
            return True
    if position[0]>=MAX and position[1]>=MIN and position[1]<MAX:#右
        if velocity[0]>0:
            return False
        else:
            return True
    """
                    |                  |
                    |                  |27
       -------------------------------------------------
                    |                  |
                    |                  |
                    |                  |
                    |                  |
                    | 7                |
       -------------------------------------------------
                    |                  |
                    |                  |
    """

        
    return False

class Point():
    def __init__(self, p, v) -> None:
        self.p = p
        self.v = v
    def __str__(self) -> str:
        return 'p = {0}, v ={1}'.format(self.p, self.v)

def part2():
    """
    Upon further analysis, it doesn't seem like any hailstones will naturally collide. It's up to you to fix that!

You find a rock on the ground nearby. While it seems extremely unlikely, if you throw it just right, you should be able to hit every hailstone in a single throw!

You can use the probably-magical winds to reach any integer position you like and to propel the rock at any integer velocity. Now including the Z axis in your calculations, 
if you throw the rock at time 0, where do you need to be so that the rock perfectly collides with every hailstone? Due to probably-magical inertia, 
the rock won't slow down or change direction when it collides with a hailstone.

In the example above, you can achieve this by moving to position 24, 13, 10 and throwing the rock at velocity -3, 1, 2. If you do this, 
you will hit every hailstone as follows:

Hailstone: 19, 13, 30 @ -2, 1, -2
Collision time: 5
Collision position: 9, 18, 20

Hailstone: 18, 19, 22 @ -1, -1, -2
Collision time: 3
Collision position: 15, 16, 16

Hailstone: 20, 25, 34 @ -2, -2, -4
Collision time: 4
Collision position: 12, 17, 18

Hailstone: 12, 31, 28 @ -1, -2, -1
Collision time: 6
Collision position: 6, 19, 22

Hailstone: 20, 19, 15 @ 1, -5, -3
Collision time: 1
Collision position: 21, 14, 12
Above, each hailstone is identified by its initial position and its velocity. Then, the time and position of that hailstone's collision with your rock are given.

After 1 nanosecond, the rock has exactly the same position as one of the hailstones, obliterating it into ice dust! Another hailstone is smashed to bits two nanoseconds 
after that. After a total of 6 nanoseconds, all of the hailstones have been destroyed.

So, at time 0, the rock needs to be at X position 24, Y position 13, and Z position 10. Adding these three coordinates together produces 47. 
(Don't add any coordinates from the rock's velocity.)

Determine the exact position and velocity the rock needs to have at time 0 so that it perfectly collides with every hailstone. 
What do you get if you add up the X, Y, and Z coordinates of that initial position?
    """
    
    points = []
    with open(input) as file:
        for x in file:
            line = x.strip().split('@')
            p = np.array(tuple(int(l) for l in line[0].split(',')))
            v = np.array(tuple(int(l) for l in line[1].split(',')))
            points.append(Point(p, v))

"""
    #x, y, z, r s t, u, v, w
    x + u* r- position_0.v[0]* r = position_0.p[0]
    y + v* r- position_0.v[1]* r = position_0.p[1]
    z + w* r- position_0.v[2]* r = position_0.p[2]
    x + u* s- position_1.v[0]* s = position_1.p[0]
    y + v* s- position_1.v[1]* s = position_1.p[1]
    z + w* s- position_1.v[2]* s = position_1.p[2]
    x + u* t- position_2.v[0]* t = position_2.p[0]
    y + v* t- position_2.v[1]* t = position_2.p[1]
    z + w* t- position_2.v[2]* t = position_2.p[2]

    #P + VT- P0.v*T = P0.p   
    #P + VT- P1.v*T = P1.p
    #P + VT- P2.v*T = P2.p



    T = -(P1.p - P0.p)/(P1.v- P0.v)
"""



part1()