data = [line.split() for line in open("data.txt", "r")]
values = [0, 0, 0]

for action in data:
    match action[0]:
        case "forward":
            values[0] += int(action[1])
            values[1] += int(action[1]) * values[2]
        case "down":
            values[2] += int(action[1])
        case "up":
            values[2] -= int(action[1])

print ("Answer to part one: " + str(values[0] * values[2]))
print ("Answer to part two: " + str(values[0] * values[1]))