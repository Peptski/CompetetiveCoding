def part_one():
    data = open("data.txt", "r")
    previous, counter = None, 0

    for line in data:
        if previous != None and int(line) > previous: counter += 1
        previous = int(line)
    
    return counter

def part_two():
    data = open("data.txt", "r")
    counter, blocks = 0, [0] * 5

    for i, line in enumerate(data):
        for x in range(0, 3): blocks[(i + x) % 5] += int(line)
        if i > 2 and (blocks[(i - 1) % 5] < blocks[i % 5]): counter += 1
        blocks[(i - 1) % 5] = 0

    return counter

print ("Answer to part one: " + str(part_one()))
print ("Answer to part two: " + str(part_two()))