input = "adventofcode/2023/input/day12.input"

def part1():
    with open(input) as file:
        sum = 0
        for line in file:
            pattern = parsePattern(line.strip())
            rule = parseRules(line.strip())
            sum += countPatterns1(pattern, rule)

        print(sum)

def part2():
    with open(input) as file:
        sum = 0
        for line in file:
            pattern = unfoldPattern(parsePattern(line.strip()))
            rule = unfoldRules(parseRules(line.strip()))
            sum += countPatterns1(pattern, rule) 
        print(sum)

def countPatterns1(pattern, rule):
    return countPatterns(0,0,0, pattern, rule, {})

def countPatterns(i: int, j: int , r: int, pattern:str, rule: list, memo):
    if j == len(pattern):
        if i == j and len(rule) == r:
            return 1
        if len(rule) -1 == r and j - i == rule[r]:
            return 1
        return 0
    if i >= len(pattern) or j>=len(pattern) or r >len(rule):
        return 0
    
    pos = ','.join([str(i), str(j),str(r)])
    if pos in memo.keys():
        return memo[pos]
    c = pattern[j]
    if c == '#':
        result = countPatterns(i, j +1, r, pattern, rule, memo)
        memo[pos] = result
        return result
    if c == '.':
        if i !=j:
            if r == len(rule) or rule[r] != j - i:
                return 0
            i = j
            r+=1
        result = countPatterns(i + 1, j + 1, r, pattern, rule, memo)
        memo[pos] = result
        return result
    result = countPatterns(i, j+1, r, pattern, rule, memo)
    if i != j:
        if r == len(rule) or rule[r] != j -i:
            memo[pos] = result
            return result
        i = j
        r +=1
    
    result += countPatterns(i +1, j +1, r, pattern, rule, memo)
    memo[pos] = result
    return result


def parseRules(line: str):
    return [int(i) for i in line.split(' ', 2)[1].split(',')]

def parsePattern(line: str):
    return line.split(' ', 2)[0]

def unfoldPattern(pattern: str):
    return ((pattern+'?')*5)[0:-1]

def unfoldRules(rules:list):
    unfolded = [0]*(len(rules)*5)
    for i in range(len(unfolded)):
        unfolded[i]= rules[i % len(rules)]
    return unfolded

part1()
part2()
