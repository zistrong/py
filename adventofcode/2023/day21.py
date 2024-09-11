input = filename = "adventofcode/2023/input/day21.input"
DOT = '.'
class Node():
    def __init__(self, i , j) -> None:
        self.i = i
        self.j = j

def process(node:Node, second: set, direct: int, dotSet: set, nodes):

    if (str(node.i + direct) + "-" + str(node.j)) in dotSet:
        second.add(nodes[node.i + direct][node.j])
    
    if (str(node.i) + "-" + str(node.j + direct)) in dotSet :
        second.add(nodes[node.i][node.j + direct])

def init():
    first = set()
    dotSet = set()
    lines = []
    with open(input) as file:
        lines = file.readlines()
    nodes = [[None for __ in range(len(lines[0].strip())) ] for _ in range(len(lines))]
    i = 0
    for s in lines:
        line = s.strip()
        for j in range(len(line)):
            c = line[j]
            node = Node(i, j)
            if c == 'S':
                first.add(node)
                dotSet.add(str(node.i) +'-' + str(node.j))
            elif c == DOT:
                dotSet.add(str(node.i) +'-' + str(node.j))
            nodes[i][j] = node
        i+=1
    return first, dotSet,nodes


def part1():
    initData = init()
    step = 64
    second = set()
    first = initData[0]
    while step > 0:
        for node in first:
            process(node, second, 1, initData[1], initData[2])
            process(node, second, -1, initData[1], initData[2])
        first = second
        second = set()
        step-=1
    
    print(len(first))


part1()




