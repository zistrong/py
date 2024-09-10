import random
import copy
input = "adventofcode/2023/input/day16.input"


class Node():
    def __init__(self) -> None:
        self.visit = 0
        self.c = None
        self.x = 0
        self.y = 0

class Beam():
    def __init__(self) -> None:
        self.id = str(random.random())
        self.direction =  None
        self.x = 0
        self.y = 0
        self.init = False


def reset(nodesList: list):
    for nodeList in nodesList:
        for node in nodeList:
            node.visit = 0


def isBlock(beam: Beam, nodesList: list):
    return (beam.x >=len(nodesList) or beam.x <0 or beam.y >=len(nodesList[beam.x]) or beam.y < 0) and not beam.init

def getScore(list):
    score = 0
    for nodeList in list:
        score +=len([x for x in nodeList if x.visit >0])
    return score

def init():
    nodesList = []
    with open(input) as file:
        i = 0
        for line in file:
            s = line.strip()
            nodeList = []
            for j in range(len(s)):
                node = Node()
                node.c = s[j]
                node.x = i
                node.y = j
                nodeList.append(node)
            i+=1
            nodesList.append(nodeList)
    
    return nodesList
def visit(map: dict, nodesList: list):
    while map:
        current:Beam = list(map.values())[0]
        while True:
            if current.direction == 'w':
                current.y-=1
            if current.direction == 'e':
                current.y+=1
            if current.direction == 'n':
                current.x-=1
            if current.direction == 's':
                current.x+=1
            if isBlock(current, nodesList):
                break
            current.init = False
            node = nodesList[current.x][current.y]
            node.visit +=1
            if current.direction =='e' and node.c =='\\' or current.direction =='w' and node.c =='/':
                newBeam = copy.deepcopy(current)
                newBeam.direction = 's'
                newBeam.id = str(random.random())
                map[newBeam.id]=newBeam
                break
            if current.direction =='w' and node.c =='\\' or current.direction =='e' and node.c =='/':
                newBeam = copy.deepcopy(current)
                newBeam.direction = 'n'
                newBeam.id = str(random.random())
                map[newBeam.id]=newBeam
                break
            if current.direction =='n' and node.c =='\\' or current.direction =='s' and node.c =='/':
                newBeam = copy.deepcopy(current)
                newBeam.direction = 'w'
                newBeam.id = str(random.random())
                map[newBeam.id]=newBeam
                break
            if current.direction =='n' and node.c =='/' or current.direction =='s' and node.c =='\\':
                newBeam = copy.deepcopy(current)
                newBeam.direction = 'e'
                newBeam.id = str(random.random())
                map[newBeam.id]=newBeam
                break
            if (current.direction == 'w' or current.direction == 'e') and node.c =='|':
                if node.visit <=1:
                    n = Beam()
                    n.x = node.x
                    n.y = node.y
                    n.direction = 'n'
                    map[n.id] = n
                    s = Beam()
                    s.x = node.x
                    s.y = node.y
                    s.direction = 's'
                    map[s.id] = s
                break
            if (current.direction == 's' or current.direction == 'n') and node.c =='-':
                if node.visit <=1:
                    n = Beam()
                    n.x = node.x
                    n.y = node.y
                    n.direction = 'w'
                    map[n.id] = n
                    s = Beam()
                    s.x = node.x
                    s.y = node.y
                    s.direction = 'e'
                    map[s.id] = s
                break
        del map[current.id]

            
def part1():
    nodesList = init()
    map = {}
    startBeam = Beam()
    startBeam.direction = 'e'
    startBeam.x = 0
    startBeam.y = -1
    startBeam.init = True
    map[startBeam.id] = startBeam
    visit(map, nodesList)
    print(getScore(nodesList))

def part2():
    nodesList = init()
    maxScore = 0
    map = {}
    for i in range(len(nodesList)):
        startBeam = Beam()
        startBeam.direction = 'e'
        startBeam.x = i
        startBeam.y = -1
        startBeam.init = True
        map[startBeam.id] = startBeam
        visit(map, nodesList)
        maxScore = max(maxScore, getScore(nodesList));
        reset(nodesList)

        startBeam.direction = 'w'
        startBeam.y = len(nodesList[0])
        startBeam.init = True
        map[startBeam.id] = startBeam
        visit(map, nodesList)
        maxScore = max(maxScore, getScore(nodesList))
        reset(nodesList)
    for i in range(len(nodesList[0])):
        startBeam = Beam()
        startBeam.direction = 's'
        startBeam.x = -1
        startBeam.y = i
        startBeam.init = True
        map[startBeam.id] = startBeam
        visit(map,nodesList)
        maxScore = max(maxScore, getScore(nodesList))
        reset(nodesList)

        startBeam.direction = 'n'
        startBeam.x = len(nodesList)
        startBeam.init = True
        map[startBeam.id] = startBeam
        visit(map,nodesList)
        maxScore = max(maxScore, getScore(nodesList))
        reset(nodesList)
    print(maxScore)

part1()
part2()