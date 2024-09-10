import hashlib
input = "adventofcode/2023/input/day14.input"
O = 'O'
DOT = '.'
SHARP = '#'

def getMD5String(s: str):
    md5_hash = hashlib.md5()  
    md5_hash.update(s.encode('utf-8'))
    return md5_hash.hexdigest() 

def getSum(contents: list) :
        length = len(contents)
        sum = 0
        for m in range(length):
          sum += len(list(filter(lambda k: k == O ,contents[m]))) * (length - m)
        return sum

def north(contents: list) :
        for i in range(len(contents)):
            line = contents[i]
            for j in range(len(line)):
                c = line[j]
                if (c == O or c == SHARP):
                    continue
                for k in range(i + 1, len(contents)):
                     nextLine = contents[k]
                     next = nextLine[j]
                     if next == SHARP:
                          break
                     if next == O:
                          nextLine = nextLine[:j] + DOT + nextLine[j+1:]
                          line =line[:j] + O + line[j+1:]
                          contents[k] = nextLine
                          contents[i] = line
                          break

def south(contents: list):
    for i in range(len(contents) - 1, -1, -1):
         line = contents[i]
         for j in range(len(line)):
              c = line[j]
              if c == O or c == SHARP:
                   continue
              for k in range(i - 1, -1, -1):
                   nextLine = contents[k]
                   next = nextLine[j]
                   if next == SHARP:
                        break
                   if next == O:
                        nextLine = nextLine[:j] + DOT + nextLine[j+1:]
                        line =line[:j] + O + line[j+1:]
                        contents[k] = nextLine
                        contents[i] = line
                        break

def east(contents: list):
     for i in range(len(contents)):
          line = contents[i]
          for j in range(len(line)-1, -1 , -1):
               c = line[j]
               if c == O or c == SHARP:
                   continue
               for k in range(j - 1 , -1 ,-1):
                    next = line[k]
                    if next == SHARP:
                        break
                    if next == O:
                        line =line[:j] + O + line[j+1:]
                        line =line[:k] + DOT + line[k+1:]
                        contents[i] = line
                        break

def west(contents: list):
     
     for i in range(len(contents)):
          line = contents[i]
          for j in range(len(line)):
               c = line[j]
               if c == O or c == SHARP:
                    continue
               for k in range(j + 1, len(line)):
                    next = line[k]
                    if next == SHARP:
                        break
                    if next == O:
                        line =line[:j] + O + line[j+1:]
                        line =line[:k] + DOT + line[k+1:]
                        contents[i] = line
                        break
            
    
def round(contents) :
    north(contents)
    west(contents)
    south(contents)
    east(contents)

def part1():

        contents = []
        with open(input) as file:
          contents = [line.strip() for line in file]
        north(contents)
        print(getSum(contents))
    
def part2():
        contents = []
        with open(input) as file:
          contents = [line.strip() for line in file]
        list = []
        k = 0
        size = 0
        while True:
          round(contents)
          stringBuilder = ''.join(contents)
          md5 = getMD5String(stringBuilder)
          if md5 in list:
               size = len(list)
               k = list.index(md5)
               break
          list.append(md5)
        for i in range((1000000000 - k - 1) % (size - k)):
             round(contents)
        print(getSum(contents))
     
part1()
part2()
