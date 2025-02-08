import re
input = "adventofcode/2023/input/day6.input"
def getCount(time, distance, count=0) :
    mid = time // 2
    while mid > 0 and mid * (time - mid) > distance :
        count+=1
        mid-=1
    return count

def part1():
    with open(input) as file:
        line1 = file.readline()
        line2 = file.readline()
        mat = re.compile(r'(\d+)')
        timeList = mat.findall(line1)
        distanceList = mat.findall(line2)
        mutiply = 1
        for k in range(len(timeList)):
            count = getCount(int(timeList[k]), int(distanceList[k]), count=0)
            mutiply = mutiply * (count * 2 -1 if int(timeList[k]) % 2 == 0 else count * 2)
        print(mutiply)

def part2():
    with open(input) as file:
        line1 = file.readline()
        line2 = file.readline()
        time = int(line1.replace('Time:','').replace(' ',''))
        distance = int(line2.replace('Distance:','').replace(' ',''))
        count = getCount(time, distance)
        mutiply = 1
        mutiply = mutiply * (count * 2 - 1 if time % 2 == 0  else count * 2)
        print(mutiply)

part2()