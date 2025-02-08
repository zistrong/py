
import time
filename = "adventofcode/2023/input/day18.input"

class Command:  
    def __init__(self, direction, step):  
        self.direction = direction  
        self.step = step  
        self.x = 0  
        self.y = 0  
  
class Cube:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
        self.c = '.'  
        self.direct = 'S'  # 7  
  
def part1():  
    commands = read_input()
    commandList = []
    u = d = l = r = 0
    for command in commands:
        s = command.strip().split(' ')
        command1 = Command(s[0][0], int(s[1]))
        commandList.append(command1)
        if command1.direction == 'U':
            u+=command1.step
        elif command1.direction == 'D':
            d+=command1.step
        elif command1.direction == 'L':
            l+=command1.step
        elif command1.direction == 'R':
            r+=command1.step
    cubes = [[Cube(i, j) for j in range(r+l)] for i in range(u+d)]
    startX = u - 1
    startY = l - 1
    cubes[startX][startY].c = '#'
    for command in commandList:
        for _ in range(command.step):
            if command.direction == 'U':
                cubes[startX][startY].direct='p' if cubes[startX][startY].direct == 'L' else None
                startX-=1
            elif command.direction == 'D':
                cubes[startX][startY].direct='p' if cubes[startX][startY].direct == 'R' else None
                startX+=1
            elif command.direction == 'L':
                cubes[startX][startY].direct='p' if cubes[startX][startY].direct == 'U' else None
                startY-=1
            elif command.direction == 'R':
                cubes[startX][startY].direct='p' if cubes[startX][startY].direct == 'D' else None
                startY+=1
            cubes[startX][startY].c = '#'
        cubes[startX][startY].direct = command.direction
    
    minX = float('inf')
    minY =  float('inf')
    maxX = 0
    maxY = 0
    count = 0
    firstCommand = commandList[0]
    lastCommand = commandList[-1]
    if (lastCommand.direction == 'L' and firstCommand.direction == 'U') or (lastCommand.direction == 'R' and firstCommand.direction == 'D')or (lastCommand.direction == 'U' and firstCommand.direction == 'L') or (lastCommand.direction == 'D' and firstCommand.direction == 'R'):
        cubes[u - 1][l - 1].direct = 'p'

    for i in range(len(cubes)):
        cc = cubes[i]
        for j in range(len(cc)):
            if cc[j].c != '.':
                minX = min(minX, i)
                minY = min(minY, j)
                maxX = max(i, maxX)
                maxY = max(j, maxY)

    for i in range(minX, maxX+1):
        for j in range(minY, maxY+1):
            if cubes[i][j].c == '#':
                count+=1
            else:
                tempX = i - 1
                tempY = j - 1
                inCount = 0
                while tempY >=minY and tempX >=minX:
                    if cubes[tempX][tempY].c == '#' and cubes[tempX][tempY].direct != 'p':
                        inCount+=1
                    tempY-=1
                    tempX-=1
                
                if inCount % 2:
                    count+=1
    print(count)

def part2():  
    commands = read_input()  
    s = 0  
    startX, startY = 0, 0  
    prev = None  
    S = 0  
  
    for command_str in commands:  
        s1 = command_str.split()  
        color = s1[2].strip('()#')  
        c = color[-1]  
        step = int(color[:-1], 16)  
        command = Command(c, step)
        s += command.step
  
        command.x = startX
        command.y = startY
  
        if command.direction == '0':
            startY += command.step  
        elif command.direction == '1':
            startX += command.step  
        elif command.direction == '2':
            startY -= command.step  
        elif command.direction == '3':
            startX -= command.step
        if prev:  
            S += prev.y * command.x - prev.x * command.y  
        prev = command
  
    S = S // 2  
    print(S + s // 2 + 1)
  
def read_input():  
    with open(filename, 'r') as file:  
        return file.readlines()  
  
part1()
part2()