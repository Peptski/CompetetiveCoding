for case in range(1, int(input()) + 1):
    ants, stickLen = [int(n) for n in input().split(" ")]
    stick = [None] * (stickLen + 1)

    antLocs = []
    for ant in range(ants):
        pos, dir = [int(n) for n in input().split(" ")]
        stick[pos] = [dir, ant + 1]
        antLocs.append(pos)

    order = []
    while len(order) < ants:
        nextState = [None] * (stickLen + 1)
        nextAntLocs = []
        falls = []
        for loc in antLocs:
            dir = stick[loc][0]
            if dir == 0:
                if loc == 0:
                    falls.append(str(stick[loc][1]))
                elif loc > 0 and stick[loc - 1] != None and stick[loc - 1][0] == 1:
                    if loc < stickLen and stick[loc + 1] != None and stick[loc + 1][0] == 0:
                        nextState[loc - 1] = [0, stick[loc][1]]
                        nextAntLocs.append(loc - 1)
                    else:
                        nextState[loc + 1] = [1, stick[loc][1]]
                        nextAntLocs.append(loc + 1)
                elif loc > 1 and stick[loc - 2] != None and stick[loc - 2][0] == 1:
                    if stick[loc - 1] != None and stick[loc - 1][0] == 0:
                        nextState[loc + 1] = [1, stick[loc][1]]
                        nextAntLocs.append(loc + 1)
                    else:
                        nextState[loc] = [1, stick[loc][1]]
                        nextAntLocs.append(loc)
                else:
                    nextState[loc - 1] = [0, stick[loc][1]]
                    nextAntLocs.append(loc - 1)
            if dir == 1:
                if loc == stickLen:
                    falls.append(str(stick[loc][1]))
                elif loc < stickLen and stick[loc + 1] != None and stick[loc + 1][0] == 0:
                    if loc > 0 and stick[loc - 1] != None and stick[loc - 1][0] == 1:
                        nextState[loc + 1] = [1, stick[loc][1]]
                        nextAntLocs.append(loc + 1)
                    else:
                        nextState[loc - 1] = [0, stick[loc][1]]
                        nextAntLocs.append(loc - 1)
                elif loc < stickLen - 2 and stick[loc + 2] != None and stick[loc + 2][0] == 0:
                    if stick[loc + 1] != None and stick[loc + 1][0] == 1:
                        nextState[loc - 1] = [0, stick[loc][1]]
                        nextAntLocs.append(loc - 1)
                    else:
                        nextState[loc] = [0, stick[loc][1]]
                        nextAntLocs.append(loc)
                else:
                    nextState[loc + 1] = [1, stick[loc][1]]
                    nextAntLocs.append(loc+1)
        stick = nextState
        antLocs = nextAntLocs
        if len(falls):
            for fall in sorted(falls):
                order.append(fall)

    print("Case #{}: {}".format(case, " ".join(order)))
    