import threading
class Node:
    def __init__(self) -> None:
        pass
    
input = "adventofcode/2023/input/day5.input"
def getNode(l) :

    node = Node()
    node.destination = next(l)
    node.source = next(l)
    node.range = next(l)
    return node


def getMinLocation(seed: int, minLocation:int, lists:list):
    for list in lists:
        seed = getSeed(seed, list)
    if seed < minLocation:
        minLocation = seed
    return minLocation

def getSeed(seed: int, list) :
    for node in list:
        if seed >= node.source and seed < node.source + node.range:
            seed = node.destination + seed - node.source
            return seed
    return seed

def getSeedsList(src: str):
    return map(int, src.strip().replace('seeds: ', '').split(' '))

def init():
    with open(input) as file:
        contents = file.readlines()
        seeds = getSeedsList(contents[0])
        lists = []
        for i in range(2, len(contents)):
            line = contents[i].strip()
            if not line:
                continue
            if line in ["seed-to-soil map:", "water-to-light map:", "soil-to-fertilizer map:", "fertilizer-to-water map:",
                        "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]:
                lists.append([])
                continue
            else:
                lists[len(lists)-1].append(getNode(getSeedsList(line)))

        return lists, seeds
def part1():
    minLocation = 9999999999999999999
    r = init()
    seeds = r[1]
    lists = r[0]
    for seed in seeds:
        minLocation = getMinLocation(seed, minLocation, lists)
    print(minLocation)

def part2():
    r = init()
    map = {}
    seeds = list(r[1])
    threads = []
    for i in range(0,len(seeds),2):
        t = threading.Thread(target=task, args=(i, seeds, r, map))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    print(min(map.values()))

def task(ii, seeds, r, map):
    min = 9999999999999999999
    for j in range(seeds[ii], seeds[ii]+seeds[ii+1]):
        min = getMinLocation(j, min, r[0])
    map[ii]=min

part2()