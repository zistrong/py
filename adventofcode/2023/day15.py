import copy
input = "adventofcode/2023/input/day15.input"
EQUAL = '='
MINUS = '-'

def getHash(s):
    hash = 0
    for c in s:
        hash = (ord(c) + hash) * 17 % 256
    return hash

def part1():
    sum = 0
    with open(input) as file:
        for line in file.readline().strip().split(','):
            sum += getHash(line.strip())
    print(sum)

class Box():
    def __init__(self, list) -> None:
        self.list = list

class Lens():
    def __init__(self) -> None:
        self.name = ''
        self.len = 0

def part2():
    boxes = [Box([]) for i in range(256)]
    with open(input) as file:
        for label in file.readline().strip().split(','):
            if EQUAL in label:
                s = label.split(EQUAL)[0]
                boxIndex = getHash(s)
                llen = int(label.split(EQUAL)[1])
                lens = None
                for item in boxes[boxIndex].list:
                    if item.name == s:
                        lens = item
                if not lens:
                    lens = Lens()
                    lens.name = s
                    boxes[boxIndex].list.append(lens)
                lens.len = llen
            else:
                s = label.replace(MINUS, '')
                boxIndex = getHash(s)
                boxes[boxIndex].list = [x for x in boxes[boxIndex].list if x.name != s]
    score = 0
    for i in range(len(boxes)):
        box = boxes[i]
        for j in range(len(box.list)):
            score += (i+1) * (j+1) * box.list[j].len
    print(score)
part1()
part2()