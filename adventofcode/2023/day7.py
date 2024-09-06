import re
input = "adventofcode/2023/input/day7.input"

CHAR_J = 'J'

class Node():
    def __init__(self, label: str, strength, part) -> None:
        self.strength = strength
        self.originalLabel = label
        self.label = label
        self.part = part
        self.type = 1
        if part == 2:
            self.initLabel()
        self.initType()
    def getPresentNumber(self, c):
        if c == 'A':
            return 14
        elif c == 'K':
            return 13
        elif c == 'Q':
            return 12
        elif c == CHAR_J:
            return 11
        elif c == 'T':
            return 10
        else:
            return 0
    def initLabel(self):
        c = ''
        for k in self.originalLabel:
            if k != CHAR_J and k not in c:
                c = c+k
        if len(c)==0:
            return
        maxC = ''
        max1 = 0
        for i in c:
            count = len(list(filter(lambda x: x == i, self.originalLabel)))
            if count > max1:
                maxC = i
                max1 = count
        self.label = self.originalLabel.replace(CHAR_J,maxC)


    def isFiveOfKind(self):
        return len(set(self.label)) == 1
    def isFourKind(self):
        return len(list(filter(lambda x: x == self.label[0], self.label))) == 4 or len(list(filter(lambda x: x == self.label[1:2], self.label))) == 4
    def isFullHouse(self):
        
        l = sorted(self.label)
        if len(l)<5:
            return False
        return (len(list(filter(lambda x: x == l[0], l))) == 2 and 
                len(list(filter(lambda x: x == l[4], l))) == 3) or (
                    len(list(filter(lambda x: x == l[0], l))) == 3 and 
                len(list(filter(lambda x: x == l[4], l))) == 2
                )
        
    def isThreeKind(self):
        distSet = list(set(self.label))
        if len(distSet) != 3:
            return False
        return (len(list(filter(lambda x: x == distSet[0], self.label))) == 3) or (len(list(filter(lambda x: x == distSet[1], self.label))) == 3) or (len(list(filter(lambda x: x == distSet[2], self.label))) == 3)
        
    def isTowPair(self):
        distSet = list(set(self.label))
        if len(distSet) != 3:
            return False
        return (len(list(filter(lambda x: x == distSet[0], self.label))) == 1) or (len(list(filter(lambda x: x == distSet[1], self.label))) == 1) or (len(list(filter(lambda x: x == distSet[2], self.label))) == 1)

    def isOnePair(self):
        distSet = list(set(self.label))
        return len(distSet) == 4

    def initType(self):
        if self.isFiveOfKind() :
            self.type = 7
        elif self.isFourKind() :
            self.type = 6
        elif self.isFullHouse() :
            self.type = 5
        elif self.isThreeKind() :
            self.type = 4
        elif self.isTowPair():
             self.type = 3
        elif self.isOnePair() :
            self.type = 2
    def __lt__(self, o):
        return self.compare(o) < 0
    def compare(self, o):
        if self.type == o.type:
            for i in range(len(self.originalLabel)):
                current = self.originalLabel[i]
                other = o.originalLabel[i]
                if self.part == 2:
                    if current == (CHAR_J) and other != (CHAR_J):
                        return -1
                    if current != (CHAR_J) and other == (CHAR_J):
                        return 1
                if current.isdigit() and not other.isdigit():
                    return -1
                if not current.isdigit() and other.isdigit():
                    return 1
                if current.isdigit() and other.isdigit():
                    k = ord(current) - ord(other)
                    if k == 0:
                        continue
                    return k
                if not current.isdigit() and not other.isdigit():
                    k = self.getPresentNumber(current) -  self.getPresentNumber(other)
                    if k == 0:
                        continue
                    return k
        else:
            return self.type - o.type
    def __repr__(self):
        return self.label + " "+str(self.part)+" "+str(self.strength) +" "+str(self.type)
def part1():
    with open(input) as file:
        nodeList = []
        for line in file:
            s = line.strip().split(' ')
            node = Node(s[0], int(s[1]), 1)
            nodeList.append(node)
        sum = 0
        i = 1
        nodeList = sorted(nodeList)
        for node in nodeList:
            sum +=(i * node.strength)
            i+=1
        
        print(sum)


def part2():
    with open(input) as file:
        nodeList = []
        for line in file:
            s = line.strip().split(' ')
            node = Node(s[0], int(s[1]), 2)
            nodeList.append(node)
        sum = 0
        i = 1
        nodeList = sorted(nodeList)
        for node in nodeList:
            sum +=(i * node.strength)
            i+=1
        print(sum)
        
part1()
part2()