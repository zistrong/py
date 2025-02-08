input = "adventofcode/2023/input/day9.input"

def part1():
    with open(input) as file:
        sum = 0
        for l in file:
            list = [int(x) for x in l.strip().split(' ')]
            lastIndex = len(list) - 1
            while list[lastIndex] !=0:
                sum += list[lastIndex]
                for i in range(lastIndex):
                    list[i] = list[i+1] - list[i]
                lastIndex -=1
        print(sum)
def part2():
    with open(input) as file:
        sum = 0
        for l in file:
            list = [int(x) for x in l.strip().split(' ')]
            lastIndex = len(list) - 1
            flag = 1
            while list[lastIndex] !=0:
                sum += list[0] * flag
                for i in range(lastIndex):
                    list[i] = list[i+1] - list[i]
                lastIndex -=1
                flag *= -1

        print(sum)
part1()
part2()