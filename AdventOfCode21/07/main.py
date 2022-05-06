import statistics as st
import math

def crab_submarines():
    data = open("data.txt", "r").read().split(",")
    for i, submarine in enumerate(data): data[i] = int(submarine)
    cost, v = [0, 0], [0, 0]

    for distance in data:
        cost[0] += abs(distance - int(st.median(data)))
        v[0] += int((abs(distance - (math.floor(st.mean(data)))) * (abs(distance - (math.floor(st.mean(data)))) + 1)) / 2)
        v[1] += int((abs(distance - (math.ceil(st.mean(data)))) * (abs(distance - (math.ceil(st.mean(data)))) + 1)) / 2)
        cost[1] = min(v[0], v[1])
    return (cost)

results = crab_submarines()
print ("Answer to part one: " + str(results[0]))
print ("Answer to part two: " + str(results[1]))