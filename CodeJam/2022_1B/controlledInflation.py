for case in range(1, int(input()) + 1):
    customers, items = input().split(" ")
    itemList = []
    for i in range(int(customers)):
        itemList.append([int(item) for item in input().split(" ")])
    totalSum = 0
    current = 0

    cost = []
    for items in itemList:
        cost.append([min(items), max(items), abs(min(items) - max(items))])

    cost.reverse()

    for i, items in enumerate(cost):
        totalSum += items[2]
        
        if i < len(cost) - 1: 
            minPenalty = min(abs(items[0] - cost[i + 1][0]), abs(items[0] - cost[i + 1][1]))
            maxPenalty = min(abs(items[1] - cost[i + 1][0]), abs(items[1] - cost[i + 1][1]))
        else:
            minPenalty = current
            maxPenalty = current

        if minPenalty <= maxPenalty:
            current = items[0]
        else:
            current = items[1]

        totalSum += min(minPenalty, maxPenalty)
    
    print("Case #{}: {}".format(case, totalSum))