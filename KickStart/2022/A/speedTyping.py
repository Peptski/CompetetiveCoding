for case in range(1, int(input()) + 1):
    targetString = input()
    inputString = input()
    diff = len(inputString) - len(targetString)

    if diff < 0:
        print("Case #{}: IMPOSSIBLE".format(case))
        continue

    for char in inputString:
        if len(targetString):
            if char == targetString[0]:
                targetString = targetString[1:]

    if len(targetString):
        print("Case #{}: IMPOSSIBLE".format(case))
    else:
        print("Case #{}: {}".format(case, diff))