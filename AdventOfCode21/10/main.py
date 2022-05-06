import statistics

def main():
    data = [list(line) for line in open("data.txt", "r").read().split("\n")]
    opening = ["(", "[", "{", "<"]
    pairs = {
        "(" : ")", ")" : "(",
        "[" : "]", "]" : "[",
        "{" : "}", "}" : "{",
        "<" : ">", ">" : "<"
    }
    result = [0, 0]

    stored = [[], [], [], []]
    for i, line in enumerate(data):
        corrupted = False
        for e in line:
            if e in opening: stored[0].append(e)
            else:
                if not pairs[e] == stored[0][-1]:
                    stored[1].append(e)
                    corrupted = True
                del stored[0][-1]
        if not corrupted: stored[2].append(stored[0])
        stored[0] = []

    for line in stored[2]:
        val = 0
        for i, e in enumerate(line):
            val *= 5
            if line[len(line) - (1 + i)] == "(": val += 1
            elif line[len(line) - (1 + i)] == "[": val += 2
            elif line[len(line) - (1 + i)] == "{": val += 3
            elif line[len(line) - (1 + i)] == "<": val += 4
        stored[3].append(val)
    result[1] = statistics.median(stored[3])

    result[0] += stored[1].count(")") * 3
    result[0] += stored[1].count("]") * 57
    result[0] += stored[1].count("}") * 1197
    result[0] += stored[1].count(">") * 25137

    return result

print ("Answer to part one: " + str(main()[0]))
print ("Answer to part two: " + str(main()[1]))