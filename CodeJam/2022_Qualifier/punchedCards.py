for i in range(int(input())):
    size = [int(x) for x in input().split()]
    base = [
        "+-+",
        "|.|",
        "+-+"
    ]
    for j, line in enumerate(base):
        base[j] = line + (line[1:3] * (size[1] - 1))
    base = base + (base[1:] * (size[0] - 1))
    base[0] = ".." + base[0][2:]
    base[1] = ".." + base[1][2:]
    print("Case #{}:".format(i + 1))
    for l in base:
        print(l)