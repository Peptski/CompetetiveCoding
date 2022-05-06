def hydro_vents(diagonals):
    data = get_data()
    points, result, val = [], {}, 0

    [[points.append(point) for point in points_from_line(line, diagonals)] for line in data]

    for point in points:
        if str(point) not in result:
            result[str(point)] = 1
        else:
            result[str(point)] += 1

    for k, v in result.items():
        if v > 1: val += 1

    return val

def points_from_line(line, diagonals):
    found_points = []

    if line[0] == line[2]:
        for i in range(abs(line[1] - line[3]) + 1): found_points.append([line[0], (i + min(line[1], line[3]))])
    elif line[1] == line[3]:
        for i in range(abs(line[0] - line[2]) + 1): found_points.append([(i + min(line[0], line[2])), line[1]])
    elif diagonals:
        for i, e in enumerate(range(abs(line[0] - line[2]) + 1)):
            if line[0] < line[2]:
                if line[1] < line[3]:
                    found_points.append([line[0] + i, line[1] + i])
                else:
                    found_points.append([line[0] + i, line[1] - i])
            if line[0] > line[2]:
                if line[1] < line[3]:
                    found_points.append([line[0] - i, line[1] + i])
                else:
                    found_points.append([line[0] - i, line[1] - i])
                
    return found_points

def get_data():
    data = open("data.txt", "r").read().split("\n")

    for i, entry in enumerate(data):
        data[i] = entry.replace(" -> ", ",")
        data[i] = data[i].split(",")
        for j, e in enumerate(data[i]):
            data[i][j] = int(e)

    return data

print ("Answer to part one: " + str(hydro_vents(False)))
print ("Answer to part two: " + str(hydro_vents(True)))