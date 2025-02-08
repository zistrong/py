import re
input = "adventofcode/2023/input/day4.input"
def subSum(count):
    return 1 if count < 0 else pow(2, count)


def getNumberList(src: str):
    return map(int, re.compile('\\d+').findall(src))

def part1():
    with open(input) as file:
        sum = 0
        for l in file:
            line = re.sub('\\d+:', '', l.strip().replace('Card ', '')).strip().split(" | ")
            winNumbers = getNumberList(line[0])
            allNumbers = getNumberList(line[1])
            count = 0
            for allNumber in allNumbers:
                if allNumber in winNumbers:
                    sum += subSum(count-1)
                    count += 1
        print(sum)
def part2():
    with open(input) as file:
        lines = file.readlines()
        numbers = [1 for x in range(len(lines))]
        i = 0
        for l in lines:
            line = re.sub('\\d+:', '', l.strip().replace('Card ', '')).strip().split(" | ")
            winNumbers = getNumberList(line[0])
            allNumbers = getNumberList(line[1])
            count = count_elements_in_b(winNumbers, allNumbers)
            for j in range(i+1, min(i+count+1, len(lines))):
                numbers[j] += numbers[i]
            i+=1
        print(sum(numbers))
        
def count_elements_in_b(a, b):
    count_dict = {}
    for item in b:
        if item in count_dict:
            count_dict[item] += 1 
        else:
            count_dict[item] = 1
    total_count = sum(count_dict.get(item, 0) for item in a)
    return total_count
part1()
part2()