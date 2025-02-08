import re
input = "adventofcode/2023/input/day2.input"
RED=12
GREEN =13
BLUE=14

def part1():
    with open(input) as file:
        sum = 0
        for content in file:
            ss = content.split(':')
            sss = ss[1].strip().split(';')
            for s in sss:
                blueNumber,greenNumber,redNumber = getNumber(s, 'blue'),getNumber(s, 'green'),getNumber(s, 'red')
                if (blueNumber > BLUE or greenNumber > GREEN or redNumber > RED):
                    break
            else:
                sum += int(ss[0].replace('Game ',''))
        print(sum)

def getNumber(s, color) -> int:
    colorReg = '(\\d+) '
    pat1 = re.compile(colorReg + color)
    mat1 = pat1.findall(s)
    return int(mat1[0] if mat1 else 0)
    
def part2() -> None:
    with open(input) as file:
        sum = 0
        for content in file:
            sss = content.split(':')[1].strip().split(';')
            fewestGreenNumber = fewestRedNumber = fewestBlueNumber = 0
            for s in sss:
                blueNumber,greenNumber,redNumber = getNumber(s, 'blue'), getNumber(s, 'green'),getNumber(s, 'red')
                fewestGreenNumber,fewestRedNumber ,fewestBlueNumber= max(greenNumber, fewestGreenNumber), max(redNumber, fewestRedNumber),max(blueNumber, fewestBlueNumber)
            sum += fewestGreenNumber * fewestBlueNumber * fewestRedNumber
        print(sum)

part1()
part2()


