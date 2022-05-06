def main(iterations):
    enhance = [list(line) for line in open("data.txt", "r").read().split("\n\n")][0]
    data = [list(i) for i in [line.split("\n") for line in open("data.txt", "r").read().split("\n\n")][1]]

    enhanced = data
    for i in range(iterations):
        enhanced = enhance_image(enhanced, enhance, i%2 != 0)
    return sum(["".join(line).count("#") for line in enhanced])

def enhance_image(data, enhance, flash):
    enhanced = [["" for j in range(len(data[0])+2)] for i in range(len(data)+2)]
    for i, row in enumerate(enhanced):
        for j, e in enumerate(row):
            adj = get_adjacent(data, [i-1, j-1])
            key = ""
            for p in adj:
                if p == None:
                    if flash: key += "1"
                    else: key += "0"
                elif data[p[0]][p[1]] == "#": key += "1"
                else: key += "0"
            key = int(key, 2)
            enhanced[i][j] = enhance[key]
    return enhanced

def get_adjacent(data, point):
    adjacent = [
        [point[0] - 1, point[1] - 1], [point[0] - 1, point[1]], [point[0] - 1, point[1] + 1],
        [point[0], point[1] - 1], [point[0], point[1]], [point[0], point[1] + 1],
        [point[0] + 1, point[1] - 1], [point[0] + 1, point[1]], [point[0] + 1, point[1] + 1]
    ]
    checked_adjacent = []
    for p in adjacent:
        if 0 <= p[0] < len(data[0]) and 0 <= p[1] < len(data): checked_adjacent.append(p)
        else: checked_adjacent.append(None)

    return checked_adjacent

print("Answer to part one: " + str(main(2)))
print("Answer to part two: " + str(main(50)))