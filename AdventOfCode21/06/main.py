def lanternfish(days):
    fish_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for fish in open("data.txt", "r").read().split(","): fish_list[int(fish)] += 1

    for i in range(days):
        next_iteration = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i, fish in enumerate(fish_list):
            if i == 0:
                next_iteration[6] = fish
                next_iteration[8] = fish
            else:
                next_iteration[i - 1] += fish
        fish_list = next_iteration

    return sum(fish_list)

print ("Answer to part one: " + str(lanternfish(80)))
print ("Answer to part two: " + str(lanternfish(256)))