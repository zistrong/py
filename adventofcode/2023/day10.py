input = "adventofcode/2023/input/day10.input"

class Node():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.c = ''
        self.point = False
        self.n = False
        self.s = False
        self.w = False
        self.e = False
        self.start = False
        self.visit = False
nodeList: list = []

CHAR_F = 'F'
CHAR_J = 'J'
CHAR_V = '|'
CHAR_H = '-'
CHAR_L = 'L'
CHAR_7 = '7'
CHAR_S = 'S'
CHAR_DOT = '.'
sNode:Node = None

def init():
    startX = 0
    startY = 0
    j = 0
    with open(input) as file:
        for line in file:
            content = line.strip()
            list = []
            for i in range(len(content)):
                c = content[i]
                node = Node()
                node.x = j
                node.y = i
                list.append(node)
                node.c = c
                if c == CHAR_S:
                    node.start = True
                    node.visit = True
                    startX = j
                    startY = i
                elif c == CHAR_DOT:
                    node.point = True
                elif c == CHAR_F:
                    node.e = True
                    node.s = True
                elif c == CHAR_J:
                    node.n = True
                    node.w = True
                elif c == CHAR_L:
                    node.n = True
                    node.e = True
                elif c == CHAR_7:
                    node.s = True
                    node.w = True
                elif c == CHAR_V:
                    node.s = True
                    node.n = True
                elif c == CHAR_H:
                    node.w = True
                    node.e = True
            nodeList.append(list)
            j+=1
        global sNode
        sNode = nodeList[startX][startY]


def getNextNode(sNode: Node):
    maxX = len(nodeList)
    if sNode.y != 0:
        current: Node = nodeList[sNode.x][sNode.y-1]
        if (not current.point and current.e and (sNode.w or sNode.start) and not current.start and not current.visit):
            return current
        
    if sNode.y != len(nodeList[sNode.x]) -1:
        current: Node = nodeList[sNode.x][sNode.y+1]
        if (not current.point and current.w and (sNode.e or sNode.start) and not current.start and not current.visit) :
            return current
    if sNode.x !=0:
        current = nodeList[sNode.x - 1][sNode.y]
        if (not current.point and current.s and (sNode.n or sNode.start) and not current.start and not current.visit) :
            return current
            
    if sNode.x != maxX -1:
        current: Node = nodeList[sNode.x+1][sNode.y]
        if (not current.point and current.n and (sNode.s or sNode.start) and not current.start and not current.visit) :
            return current
    return None
        

def getMaxPath(startNode: Node):
    step = 1
    while startNode:
        step+=1
        startNode.visit = True
        startNode = getNextNode(startNode)
    return step

def part1():
    init()
    print(sNode)
    maxStep = getMaxPath(sNode)
    print(maxStep//2)


def part2():
    if (sNode.x > 0 and sNode.y < len(nodeList[sNode.x]) - 1
                and nodeList[sNode.x - 1][sNode.y].s
                and nodeList[sNode.x][sNode.y + 1].w) :
        sNode.c = CHAR_L
        
    if (sNode.y > 0 and sNode.x < len(nodeList) - 1
                and nodeList[sNode.x + 1][sNode.y].n
                and nodeList[sNode.x][sNode.y - 1].e) :
        sNode.c = CHAR_7
    count = 0
    for list in nodeList:
        for node in list:
            if not node.visit:
                x = node.x
                y = node.y
                c = 0
                while x >=0 and y>=0:
                    if (nodeList[x][y].visit and not(nodeList[x][y].c == CHAR_7 or nodeList[x][y].c == CHAR_L)) :
                        c +=1
                    x -=1
                    y -=1
                if c % 1 :
                    count+=1
    print(count)
                        
        


part1()
part2()