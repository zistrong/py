from util import readFile;
def part1():
    count = 0
    now = -1
    with readFile(1) as file:
        for line in file:
            num = int(line.strip())
            if now != -1 and num > now:
                count+=1
            now = num
    print(count)

part1()