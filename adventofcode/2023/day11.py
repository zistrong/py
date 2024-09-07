input = "adventofcode/2023/input/day11.input"

class Galaxy():
    def __init__(self,x, y) -> None:
        self.x =x
        self.y =y

def init():
    space = []
    with open(input) as file:
        space = file.readlines()
    rows = []
    for i in range(len(space)):
        if '#' not in space[i]:
            rows.append(i)

    galaxies = []
    columns = []
    for i in range(len(space[0].strip())):
        flag = True
        for j in range(len(space)):
            if space[j][i] == '#':
                flag = False
                galaxies.append(Galaxy(j, i))
        if flag:
            columns.append(i)

    return {'galaxies': galaxies, 'rows': rows, 'columns': columns}
def getStep(**args):
    step = 0
    galaxies = args['galaxies']
    rows = args['rows']
    columns = args['columns']
    p = args['p']
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            start = galaxies[i]
            end = galaxies[j]
            step = step + abs(start.x - end.x)+abs(start.y - end.y)
            for row in rows:
                if row > min(start.x, end.x) and row < max(start.x, end.x):
                    step = step + p - 1
            for column in columns:
                if column > min(start.y, end.y) and column < max(start.y, end.y):
                    step = step + p - 1
    return step

def part1and2():
    map = init()
    map['p']= 2
    step = getStep(**map)
    print(step)

    map['p']= 1000000
    step = getStep(**map)
    print(step)

part1and2()


