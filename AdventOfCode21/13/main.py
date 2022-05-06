def partone():
    data = [line.split("\n") for line in open("data.txt", "r").read().split("\n\n")]
    folds = data[1]
    dots = [e.split(",") for e in data[0]]

    return len(fold(dots, folds[0]))

def parttwo():
    data = [line.split("\n") for line in open("data.txt", "r").read().split("\n\n")]
    folds = data[1]
    newdots = [e.split(",") for e in data[0]]

    for f in folds: newdots = fold(newdots, f)

    code, ymax, xmax = [], 0, 0
    for dot in newdots:
        if int(dot[0]) > xmax: xmax = int(dot[0])
        if int(dot[1]) > ymax: ymax = int(dot[1])

    for i in range(ymax + 1): code.append([" "] * (xmax + 1))

    for i, row in enumerate(code):
        for j, e in enumerate(row):
            if [str(j), str(i)] in newdots: code[i][j] = "#"

    print("Answer to part two: ")

    for row in code: print("".join(row))

def fold(dots, fold):
    newdots = dots.copy()
    match fold[:13]:
        case "fold along x=": 
            fold = int(fold[13:])
            for dot in dots:
                if int(dot[0]) == fold: newdots.remove(dot)
                if int(dot[0]) > fold: 
                    newdot = dot.copy()
                    newdot[0] = str(int(newdot[0]) - (int(newdot[0]) - fold) * 2)
                    if newdot not in newdots: newdots.append(newdot)
                    newdots.remove(dot)
        case "fold along y=":
            fold = int(fold[13:])
            for dot in dots:
                if int(dot[1]) == fold: newdots.remove(dot)
                if int(dot[1]) > fold: 
                    newdot = dot.copy()
                    newdot[1] = str(int(newdot[1]) - (int(newdot[1]) - fold) * 2)
                    if newdot not in newdots: newdots.append(newdot)
                    newdots.remove(dot)
    return newdots


print ("Answer to part one: " + str(partone()))
parttwo()