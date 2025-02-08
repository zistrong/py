import re
input = "adventofcode/2023/input/day3.input"
def isSymbol(i, j, contents) -> bool:
    if i<0 or j < 0 or i >len(contents)-1 or j>len(contents[i].strip()) -1:
        return False
    return contents[i][j] != '.'

def adjacentSymbol(line: str, startIndex: int, endIndex: int, contents) -> bool:
    if isSymbol(line, startIndex -1, contents):
        return True
    if isSymbol(line, endIndex, contents):
        return True
    
    for i in range(startIndex-1, endIndex+1):
        if isSymbol(line-1, i , contents):
            return True
        
    for i in range(startIndex-1, endIndex+1):
        if isSymbol(line+1, i , contents):
            return True
        
    return False

def part1():
    contents = []
    with open(input) as file:
        contents = file.readlines()

    sum = 0
    for i in range(len(contents)):
        content = contents[i].strip()
        startIndex = -1
        endIndex = -1
        for j in range(len(content)):
            if startIndex == -1 and content[j].isdigit():
                startIndex = j
            if startIndex != -1 and not content[j].isdigit():
                endIndex = j
            if startIndex != -1 and endIndex != -1:
                if adjacentSymbol(i, startIndex, endIndex, contents):
                    sum+=int(content[startIndex:endIndex])
                startIndex = -1
                endIndex = -1
        
        if startIndex != -1:
            endIndex = len(content)
            if adjacentSymbol(i, startIndex, endIndex, contents):
                sum += int(content[startIndex:endIndex])

    print(sum)

def getCurrentValue(x: int, y: int, contents) -> int:
    """
     * 467..114..
     * ...*......
     * ..35..633.
     * ......#...
     * 617*......
     * .....+.58.
     * ..592.....
     * ......755.
     * ...$.*....
     * .664.598..
     """
    firstValue = -1
    #left and right value
    if y >0 or y<len(contents[x].strip()) -1:
        sb = ''
        #get left value
        i = y-1
        while i>=0 and contents[x][i].isdigit():
            sb = sb + contents[x][i]
            i-=1
        if sb :
            firstValue = int(sb[::-1])
            sb = ''
        #get right value
        i = y+1
        while i <len(contents[x]) and contents[x][i].isdigit():
            sb = sb + contents[x][i]
            i+=1
        if sb:
            if firstValue == -1:
                firstValue = int(sb)
            else:
                return firstValue * int(sb)      
    #top
    if x >0:
        i = x-1
        content = contents[i].strip()
        j = max(0, y-1)
        # 如果（i,j)是数字， 往左找， 否则退出
        while j > -1 and content[j].isdigit():
            j -=1
        left = j
        j = min(len(content)-1, y+1)
        # 如果（i,j)是数字， 往右找， 否则退出
        while j< len(content) and content[j].isdigit():
            j +=1
        right = j
        # 确定了一个区间， 从这个区间中找数字， 找到两个， 直接乘积返回
        sub = content[left+1: right]
        if not sub == '.':
            regEx = "\\d+"
            pat = re.compile(regEx)
            mat = pat.findall(sub)
            if mat:
                one = mat[0]
                if firstValue != -1:
                    return firstValue * int(one)
                else:
                    firstValue = int(one)
            if len(mat) > 1:
                two = mat[1]
                if firstValue != -1:
                    return firstValue * int(two)
                else:
                    firstValue = int(two)
    # bottom
    if x <len(contents) -1:
        i = x +1
        content = contents[i].strip()
        j = max(0, y -1)
        # 如果（i,j)是数字， 往左找， 否则退出
        while j > -1 and content[j].isdigit():
            j -=1
        left = j
        j = min(len(content) -1, y+1)
        # 如果（i,j)是数字， 往右找， 否则退出
        while j<len(content) and content[j].isdigit():
            j+=1
        right = j
        # 确定了一个区间， 从这个区间中找数字， 找到两个， 直接乘积返回
        sub = content[left+1:right]
        if not sub == '.':
            regEx = "\\d+"
            pat = re.compile(regEx)
            mat = pat.findall(sub)
            if mat:
                one = mat[0]
                if firstValue != -1:
                    return firstValue * int(one)
                else:
                    firstValue = int(one)
            if len(mat)>1:
                two = mat[1]
                if firstValue != -1:
                    return firstValue * int(two)
                else:
                    firstValue = int(two)
    return 0


def part2():
    sum = 0
    contents = []
    with open(input) as file:
        contents = file.readlines()
    for i in range(len(contents)):
        content = contents[i].strip()
        for j in range(len(content)):
            if content[j] == '*':
                sum +=  getCurrentValue(i, j, contents)
    print(sum)    
            
part1()
part2()