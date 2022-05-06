def part_one():
    data = open("data.txt", "r")
    values, result= [0] * 13, 0

    for row in data:
        for i, bit in enumerate(row):
            if bit == "1":
                values[i] += 1
        values[12] += 1

    for i, v in enumerate(values):
        if i < 12 and v >= values[12] / 2: result += (2 ** (11-i))
    
    return (result * ((2 ** 12) - (result + 1)), result, ((2 ** 12) - (result + 1)))

def part_two():
    co2 = oxygen = open("data.txt", "r").read().split("\n")
    result = [0, 0]

    for list in [[co2, "least", 0], [oxygen, "most", 1]]:
        while len(list[0]) > 1:
            for i in range(12):
                if len(list[0]) > 1: list[0] = match_on_index(list[0], i, list[1])

        for i, v in enumerate(list[0][0]):
            if v == "1": result[list[2]] += (2 ** (11-i))

    return(result)

def match_on_index(strings, index, least_most):
    value = 0
    for row in strings:
        if row[index] == "1": value += 1
        else: value -= 1

    match least_most:
        case "most":
            if value >= 0: value = 1
            else: value = 0
        case "least":
            if value >= 0: value = 0
            else: value = 1
    
    return [row for row in strings if row[index] == str(value)]

print ("Answer to part one: " +  str(part_one()[0]))
print ("Answer to part two: " +  str(part_two()[0] * part_two()[1]))