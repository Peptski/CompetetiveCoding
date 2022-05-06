import math

def main():
    data = open("data.txt", "r").read().split("\n")

    string = data[0]
    for num in data:
        if num != data[0]: string = "[" + string + "," + num + "]"
        reduced = True
        while reduced: string, reduced = reduce(string)
    print("Part one: " + str(eval(string.replace("[", "((3*").replace(",", ")+(").replace("]", "*2))"))))

    highest = 0
    for num in data:
        for num2 in data:
            if num != num2:
                string, reduced= "[" + num + "," + num2 + "]", True
                while reduced: string, reduced = reduce(string)
                if eval(string.replace("[", "((3*").replace(",", ")+(").replace("]", "*2))")) > highest: highest = eval(string.replace("[", "((3*").replace(",", ")+(").replace("]", "*2))"))
    print("Part two: " + str(highest))

def reduce(string):
    depth = 0
    for i, e in enumerate(string):
        match e:
            case "[":depth += 1
            case "]":depth -= 1
            case _:
                if depth >= 5 and e not in ", []":
                    x1, p1 = nextNum(string, i-1)
                    x2, p2 = nextNum(string, p1+len(str(x1)))
                    next, p3 = nextNum(string, p2+len(str(x2)))
                    prev, p4 = prevNum(string, i)
                    if p4 != math.inf and p3 != math.inf:
                        string = string[:p3] + str(next+x2) + string[p3+len(str(next)):]
                        string = string[:p4] + str(prev+x1) + string[p4+len(str(prev)):]
                        string = string[:p1-1+(len(str(prev+x1))- len(str(prev)))] + "0" + string[p2+len(str(x2))+(len(str(prev+x1))- len(str(prev)))+1:]
                    elif p3 != math.inf:
                        string = string[:p1-1] + "0" + string[p2+len(str(x2))+1:p3] + str(next+x2) + string[p3+len(str(next)):]
                    elif p4 != math.inf:
                        string = string[:p4] + str(prev+x1) + string[p4+len(str(prev)):p1-1] + "0" + string[p2+len(str(x2))+1:]
                    else:
                        string = string[:p1-1] + "0" + string[p2+len(str(x2)):]
                    return string, True
    for i, e in enumerate(string):
        if e not in ", []" and string[i+1] not in ", []":
            string = string[:i] + "[" + str(math.floor(int(e+string[i+1])/2)) + "," + str(math.ceil(int(e+string[i+1])/2)) + "]" + string[i+2:]
            return string, True
    return string, False

def nextNum(string, start):
    found, x, number = False, 0, 0
    while not found and (start + x) < len(string)-1:
        x += 1
        if string[start+x] not in ", []": found = True
    if found:
        if string[start+x+1] not in ", []": number = int(string[start+x] + string[start+x+1])
        else: number = int(string[start+x])
        return number, start+x
    else: return 0, math.inf

def prevNum(string, start):
    found, x, number = False, 0, 0
    while not found and start + x >= 1:
        x -= 1
        if string[start+x] not in ", []": found = True
    if found:
        if string[start+x-1] not in ", []":
            x -=1
            number = int(string[start+x] + string[start+x+1])
        else: number = int(string[start+x])
        return number, start+x
    else: return 0, math.inf

main()