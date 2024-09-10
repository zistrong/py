input = filename = "adventofcode/2023/input/day19.input"

def getTarget(conditions: list, rate:dict):
    for command in conditions:
        if not ':' in command:
            return command
        co = command.split(':')[0]
        key = co[0]
        c = co[1]
        if c == '>' and rate[key] > int(co[2:]) or c == '<' and rate[key]<int(co[2:]):
            return command.split(':')[1]
    return 'R'

def part1():
    workFlows = {}
    rates = []
    israte = False
    with open(input) as file:
        for line in file:
            string = line.strip()
            if not string:
                israte = True
                continue
            if israte:
                args = string.replace("{", "").replace("}", "").split(",")
                rate = {arg[0]: int(arg[2:]) for arg in args}
                rates.append(rate)
            else:
                name = string.split('{')[0]
                commands = string.split("{")[1].replace("}", "").split(",")
                workFlows[name] = commands
    sum1 = 0
    for item in rates:
        result = ''
        currentFlow = workFlows.get('in')
        while result != 'A' and result != 'R':
            result = getTarget(currentFlow, item)
            currentFlow = workFlows.get(result)
        if result == 'A':
            sum1 += sum(item.values())
    print(sum1)

part1()