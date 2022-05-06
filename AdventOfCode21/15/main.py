import heapq
import math

def partone(big):
    if big: padding = 5
    else: padding = 1
    data = [list(str(e)) for e in open("data.txt", "r").read().split("\n")]
    risk = [[math.inf for x in range(len(data[0]) * padding)] for row in range(len(data) * padding)]

    queue = []
    heapq.heappush(queue, (0, [0, 0]))

    while len(queue) > 0:
        q = heapq.heappop(queue)
        if q[1] == [((100 * padding) - 1), ((100 * padding)-1)]: return q[0]
        for edge in get_adjacent(len(data), q[1], padding):
            y, ypad, x, xpad= edge[0], 0, edge[1], 0
            if edge[0] > 99: ypad, y = divmod(edge[0], 100)
            if edge[1] > 99: xpad, x = divmod(edge[1], 100)
            v = int(data[y][x]) + xpad + ypad
            if v > 9:
                v = v % 9
                if v == 0: v = 9
            if (q[0] + v) < risk[edge[0]][edge[1]]:
                risk[edge[0]][edge[1]] = (q[0] + v)
                heapq.heappush(queue, (q[0] + v, edge))

def get_adjacent(max, point, padding):
    return [[x, y] for (x, y) in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)] if 0 <= x < (max * padding) and 0 <= y < (max * padding)]

print ("Answer to part one: " + str(partone(False)))
print ("Answer to part two: " + str(partone(True)))