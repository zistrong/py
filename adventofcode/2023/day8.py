import math
input = "adventofcode/2023/input/day8.input"

class Node():
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

def part1():
    contents = []
    with open(input) as file:
        contents = file.readlines()
    
    map = {}
    instructions = contents[0].strip()
    for i in range(2, len(contents)):
        content = contents[i].strip().split("=")
        location = content[0].strip()
        d = content[1].strip().replace(" ", "").replace("(", "").replace(")", "")
        node = Node(d.split(",")[0].strip(), d.split(",")[1].strip())
        map[location] = node
    
    location = 'AAA'
    step = 0
    insLength = len(instructions)
    while 'ZZZ' != location:
        instruction = instructions[step % insLength]
        node = map[location]
        location = node.left if instruction == 'L' else node.right
        step+=1
    print(step)

def part2():
    contents = []
    with open(input) as file:
        contents = file.readlines()
    
    map = {}
    instructions = contents[0].strip()
    startANodes = []
    for i in range(2, len(contents)):
        content = contents[i].strip().split("=")
        location = content[0].strip()
        if location.endswith('A'):
            startANodes.append(location)
        d = content[1].strip().replace(" ", "").replace("(", "").replace(")", "")
        node = Node(d.split(",")[0].strip(), d.split(",")[1].strip())
        map[location] = node
    
    numbers = []
    insLength = len(instructions)
    for startANode in startANodes:
        step = 0
        while not startANode.endswith('Z'):
            node = map[startANode]
            instruction = instructions[step % insLength]
            startANode = node.left if instruction == 'L' else node.right
            step += 1
        numbers.append(step)
    
    minmul = 1
    for i in numbers:
        minmul = (minmul * i) / math.gcd(int(minmul), i)
    print(int(minmul))

part1()
part2()