import re
input = "adventofcode/2023/input/day1.input"
with open(input) as file:

    # """第一种方法"""
    # a = [re.sub('[A-Za-z]','', line.rstrip()) for line in file.readlines()]
    # a1 = [int(l[0])*10 + int(l[-1]) for l in a]
    # print(sum(a1))


    # """第二种方法"""
    # a = []
    # for line in file:
    #     a.append(re.sub('[A-Za-z]','', line.rstrip()))
    # a1 = [int(l[0])*10 + int(l[-1]) for l in a]
    # print(sum(a1))

    """第三种方法"""
    sum = 0
    for line in file:
        l = re.sub('[A-Za-z]','', line.rstrip())
        sum += (int(l[0]) * 10 + int(l[-1]))
    print(sum)



numbers = ["one","two","three","four","five","six","seven","eight","nine"]
with open(input) as file:
    sum = 0
    for line in file:
        firstNumber = lastNumber = None
        for i in range(len(line.rstrip())):
            c = line[i]
            if c.isdigit():
                if not firstNumber:
                    firstNumber = str(c)
                lastNumber = str(c)
                continue
            for j in range(len(numbers)):
                n = numbers[j]
                endIndex = min(len(n) + i, len(line.rstrip()))
                if (line[i:endIndex] == n):
                    if not firstNumber:
                        firstNumber = str(j + 1)
                    lastNumber = str(j + 1)
        if not lastNumber:
            lastNumber = firstNumber
        sum += int(firstNumber + lastNumber)
    print(sum)
