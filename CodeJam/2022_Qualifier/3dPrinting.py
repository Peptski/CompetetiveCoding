for case in range(int(input())):
    res = "IMPOSSIBLE"
    colors = ["c", "m", "y", "k"]
    machines = [input().split(), input().split(), input().split()]
    minimum = [min([int(machine[color]) for machine in machines]) for color in range(len(colors))]
    if sum(minimum) < 1000000:
        print("Case #{}: IMPOSSIBLE".format(case + 1))
    else:
        choice = [0, 0, 0, 0]
        while sum(choice) < 1000000:
            for i, color in enumerate(minimum):
                choice[i] += min(minimum[i], 1000000 - sum(choice))
        print("Case #{}: {}".format(case + 1, " ".join([str(num) for num in choice])))