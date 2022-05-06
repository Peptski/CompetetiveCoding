from typing import DefaultDict

def polymer(iterations):
    start, combinations = get_data()

    for i in range(iterations):
        nextIter = {}
        for k in combinations.keys(): nextIter[k] = 0

        for p in start.keys():
            for e in combinations[p]: nextIter[e] += start[p]
        start = nextIter

    chars = {}
    for k in start.keys():
        if k[0] not in chars.keys(): chars[k[0]] = start[k]
        else: chars[k[0]] += start[k]
        if k[1] not in chars.keys(): chars[k[1]] = start[k]
        else: chars[k[1]] += start[k]
    # Add one to chars at start & end of list since all other chars in two pairs
    chars["C"] += 1
    chars["O"] += 1

    return int(max(chars.values())/2 - min(chars.values())/2)
    
def get_data():
    data = [line.split("-") for line in open("data.txt", "r").read().split("\n\n")]
    rules = [line.split(" -> ") for line in open("data.txt", "r").read().split("\n")][2:]
    
    combinations = DefaultDict(set)
    for combo in rules:
        combinations[combo[0]].add(combo[0][0] + combo[1])
        combinations[combo[0]].add(combo[1] + combo[0][1])

    start = {}
    for k in combinations.keys(): start[k] = 0
    for i, e in enumerate(list(data[0][0])):
        if i + 1 != len(list(data[0][0])):
            start["".join(e + list(data[0][0])[i + 1])] += 1

    return start, combinations

print ("Answer to part one: " + str(polymer(10)))
print ("Answer to part two: " + str(polymer(40)))