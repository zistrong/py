input = "adventofcode/2023/input/day13.input"
DOT = '.'
SHARP = '#'

class Node():
    def __init__(self, direct, index, score) -> None:
        self.direct = direct
        self.index = index
        self.score = score
    def __str__(self) -> str:
        return 'direct = {0}, index = {1}, socre = {2}'.format(self.direct, self.index, self.score)

class NodePair():
    def __init__(self, h: list, v:list) -> None:
        self.h = h
        self.v = v
    def __str__(self) -> str:
        return 'h = ' + len(self.h) + ", v =" + len(self.v)

def replaceChar(s: str, i: int):
    return s[:i] + DOT + s[i+1:] if s[i]== SHARP else s[:i] + SHARP + s[i+1:]

def getReflectIndex(currentMirror):
    index = 0
    list = []
    for i in range(len(currentMirror) -1):
        t = 0
        b = len(currentMirror) -2 - i
        flag = False
        while b -t >= 1:
            if currentMirror[t] != currentMirror[b]:
                break
            if b - t == 1:
                flag = True
                break
            t+=1
            b-=1
        if flag:
            index = b
            break
    if index != 0:
        list.append(Node(False, index, index))
    for i  in range(len(currentMirror) -1,0,  -1):
        b = len(currentMirror) -1
        t = len(currentMirror) -i
        flag = False
        while b - t >=1:
            if currentMirror[t] != currentMirror[b]:
                break
            if b - t == 1:
                flag = True
                break
            t+=1
            b-=1
        if flag:
            index = b
            break
    if list and list[0].index != index:
        list.append(Node(False, index, index))
    if not list:
        list.append(Node(False, index, index))
    return list

def getScore(currentMirror):
    h = getReflectIndex(currentMirror)
    list = [Node(True, x.index, x.score * 100) for x in h]
    rotate = []
    for i in range(len(currentMirror[0])):
        stringBuilder = ''
        for s in currentMirror:
            stringBuilder = stringBuilder+s[i]
        rotate.append(stringBuilder)
    return NodePair(list, getReflectIndex(rotate))

def getRealNode(nodePair):
    return nodePair.h[0] if nodePair.h[0].score > nodePair.v[0].score else nodePair.v[0]

def getSmudgeNode(pair: NodePair, node: Node):
    if len(pair.v) > 1:
        v = pair.v[0]
        if v.score != node.score:
            return v
        else:
            return pair.v[1]
    if len(pair.h) > 1:
        h = pair.h[0]
        if h.score != node.score:
            return h
        else:
            return pair.h[1]
    if (pair.v[0].score != 0 and pair.v[0].score != node.score) :
            return pair.v[0]
        
    if (pair.h[0].score != 0 and pair.h[0].score != node.score) :
        return pair.h[0]
        
    return Node(False, 0, 0)

def getSmudgeScore(currentMirror: list, node: Node):
    for j in range(len(currentMirror)):
        stringBuilder = currentMirror[j]
        for i in range(len(stringBuilder)):
            stringBuilder = replaceChar(stringBuilder, i)
            currentMirror[j]= stringBuilder
            temp = getSmudgeNode(getScore(currentMirror), node)
            if (temp.score != 0) :
                return temp.score
            stringBuilder = replaceChar(stringBuilder, i)
            currentMirror[j]= stringBuilder

def part2():
    sumPart2 = 0
    sumPart1 = 0
    with open(input) as file:
        currentMirror = []
        for l in file:
            line = l.strip()
            if not line:
                node = getRealNode(getScore(currentMirror))
                sumPart1 += node.score
                sumPart2 += getSmudgeScore(currentMirror, node)
                currentMirror = []
                continue
            currentMirror.append(line)
        
        node = getRealNode(getScore(currentMirror))
        sumPart1 += node.score
        sumPart2 += getSmudgeScore(currentMirror, node)
    print(sumPart1, sumPart2)

part2()

