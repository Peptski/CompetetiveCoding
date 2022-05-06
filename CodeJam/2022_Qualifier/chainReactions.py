for case in range(1, int(input()) + 1):
    modules = {0 : [[], 0]}

    funFactor  = {}
    pointers = {}
    length = int(input()) + 1

    first = input().split()
    second = input().split()

    for i in range(length - 1):
        funFactor[i + 1] = int(first[i])
        pointers[i + 1] = int(second[i])

    for i in range(1, length):
        modules[i] = [[], funFactor[i]]
        modules[pointers[i]][0].append(i)
        modules[pointers[i]][1] = max(funFactor[i], modules[pointers[i]][1])

    initiators = [index for index in modules.keys() if modules[index][0] == []]
    
    maximum = 0
    while len(modules):
        key = min(modules.keys())
        localMax = funFactor.setdefault(key, 0)
        funFactor[key] = 0
        while len(modules[key][0]):
            if len(modules[key][0]) == 1: 
                path = modules[key][0][0]
                del modules[key]
                key = path
            else: 
                paths = {modules[path][1] : path for path in modules[key][0]}
                path = paths[min(paths.keys())]
                modules[key][0].remove(path)
                key = path
            localMax = max(localMax, funFactor[key])
            funFactor[key] = 0
        maximum += localMax
        del modules[key]

    print("Case #{}: {}".format(case, maximum))