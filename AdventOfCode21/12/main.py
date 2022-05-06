from typing import DefaultDict

def caveMaps(handling):
    data = [line.split("-") for line in open("data.txt", "r").read().split("\n")]

    tunnels = DefaultDict(set)
    for tunnel in data:
        tunnels[tunnel[0]].add(tunnel[1])
        tunnels[tunnel[1]].add(tunnel[0])

    result = 0
    paths = []
    for val in tunnels["start"]: paths.append(["start", val])

    while len(paths) > 0:
        for val in tunnels[paths[0][-1]]:
            if handling:
                if val == "start":continue
                lower = [e for e in (paths[0] + [val]) if e.islower()]
                if not (len(set(lower)) == len(lower) or len(set(lower)) == (len(lower) - 1)): continue
            else: 
                if val in paths[0] and val.islower(): continue

            new = paths[0] + [val]
            if new[-1] == 'end':
                result += 1
                continue
            paths.append(new)
        del paths[0]

    return result

print ("Answer to part one: " + str(caveMaps(False)))
print ("Answer to part two: " + str(caveMaps(True)))