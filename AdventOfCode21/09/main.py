def part_one():
    result = 0

    for point in lowpoints: result += (int(data[point[0]][point[1]]) + 1)
    return result

def part_two():
    result = [0]

    for point in lowpoints:
        points = [point]
        undiscovered = [point]
        while len(undiscovered) > 0:
            for adj in get_adjacent(data, undiscovered[0]):
                if data[adj[0]][adj[1]] != "9" and adj not in points:
                    undiscovered.append(adj)
                    points.append(adj)
            del undiscovered[0]
        if len(result) < 3: result.append(len(points))
        elif len(points) > min(result):
            result.append(len(points))
            result.remove(min(result))

    return result[0] * result[1] * result[2]

def get_lowpoints(data):
    lowpoints = []
    for i, line in enumerate(data):
        for j, point in enumerate(line):
            adjacent = get_adjacent(data, [i, j])
            for k, point in enumerate(adjacent):
                adjacent[k] = data[point[0]][point[1]]
            if data[i][j] < min(adjacent):
                lowpoints.append([i, j])
    return lowpoints

def get_adjacent(data, point):
    return [[x, y] for (x, y) in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)] if 0 <= x < (len(data[0])) and 0 <= y < (len(data))]

data = [list(line) for line in open("data.txt", "r").read().split("\n")]
lowpoints = get_lowpoints(data)
print ("Answer to part one: " + str(part_one()))
print ("Answer to part two: " + str(part_two()))