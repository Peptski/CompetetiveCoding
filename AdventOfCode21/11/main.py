def simulation(days):
    data = [list(line) for line in open("data.txt", "r").read().split("\n")]
    result = [0, 0]

    for i in range(days):
        points = []
        flashed = []
        for j, line in enumerate(data):
            for k, e in enumerate(line):
                data[j][k] = str(int(e) + 1)
                if int(data[j][k]) > 9:
                    data[j][k] = "0"
                    result[0] += 1
                    flashed.append([j, k])
                    for p in get_adjacent(data, [j, k]): points.append(p)           
                    
        while len(points) > 0:
            if points[0] not in flashed:
                data[points[0][0]][points[0][1]] = str(int(data[points[0][0]][points[0][1]]) + 1)
                if int(data[points[0][0]][points[0][1]]) > 9:
                    data[points[0][0]][points[0][1]] = "0"
                    result[0] += 1
                    flashed.append(points[0])
                    for p in get_adjacent(data, [points[0][0], points[0][1]]): points.append(p)
            del points[0]
            if len(flashed) == 100 and result[1] == 0: result[1] = i + 1
    return result

def get_adjacent(data, point):
    adjacent, i, j= [], int(point[0]), int(point[1])
    if i > 0:
        adjacent.append([i - 1, j])
        if j > 0: adjacent.append([i - 1, j - 1])
        if j < len(data) - 1: adjacent.append([i - 1, j + 1])
    if i < len(data) - 1:
        adjacent.append([i + 1, j])
        if j > 0: adjacent.append([i + 1, j - 1])
        if j < len(data) - 1: adjacent.append([i + 1, j + 1])
    if j > 0: adjacent.append([i, j - 1])
    if j < len(data) - 1: adjacent.append([i, j + 1])

    return adjacent

print ("Answer to part one: " + str(simulation(100)[0]))
print ("Answer to part two: " + str(simulation(250)[1]))