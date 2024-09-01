import sys


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
                if root:
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
    if f1['v'][0]/f1['v'][1] == f2['v'][0]/f2['v'][1] :#斜率相同，直线平行，无解
        return ()
    else :
        D = f2['v'][1]/f2['v'][0] - f1['v'][1]/f1['v'][0] 
        D1 = (f2['v'][1]*f2['p'][0]/f2['v'][0]-f2['p'][1]) - (f1['v'][1]*f1['p'][0]/f1['v'][0]-f1['p'][1])
        D2 = (f1['v'][1]/f1['v'][0]) * (f2['v'][1]*f2['p'][0]/f2['v'][0]-f2['p'][1]) - (f2['v'][1]/f2['v'][0]) * (f1['v'][1]*f1['p'][0]/f1['v'][0]-f1['p'][1])
        return(D1/D, D2/D)

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

part1()