from random import choice

for case in range(1, int(input()) + 1):
    totalNodes, actions = [int(integer) for integer in input().split()]
    nodes = [i for i in range(1, totalNodes + 1)]
    total = 0
    first = [int(item) for item in input().split()]
    nodes.remove(first[0])
    total += first[1] - 1

    while actions > 0:
        print("T {}".format(choice(nodes)), flush=True)
        ans = [int(item) for item in input().split()]
        nodes.remove(ans[0])
        total += ans[1] - 1
        actions -= 1

    if totalNodes <= 100000: normalizer = 2
    else: normalizer = 4

    print("E {}".format(int((((total / (totalNodes - len(nodes))) * totalNodes) / normalizer) + (totalNodes - 1))), flush=True)