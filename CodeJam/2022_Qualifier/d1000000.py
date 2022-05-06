for case in range(int(input())):
    size = 0
    length = int(input())
    dice = {}
    for die in input().split():
        if int(die) in dice.keys(): dice[int(die)] += 1
        else: dice[int(die)] = 1

    for key in sorted(dice.keys()):
        if key > size:
            size += min(dice[key], key - size)

    print("Case #{}: {}".format(case + 1, size))
