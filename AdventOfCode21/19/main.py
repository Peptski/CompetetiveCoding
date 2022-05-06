def main():
    data = [[line.split(",") for line in row if line[:3] != "---"] for row in [line.split("\n") for line in open("data.txt", "r").read().split("\n\n")]]
    
    cmpset = set()
    for row in data:
        comparisons = set()
        for e1 in row:
            for e2 in row:
                if e1 == e2: continue
                x = max(abs(int(e1[0])), abs(int(e2[0]))) - min(abs(int(e1[0])), abs(int(e2[0])))
                y = max(abs(int(e1[1])), abs(int(e2[1]))) - min(abs(int(e1[1])), abs(int(e2[1])))
                z = max(abs(int(e1[2])), abs(int(e2[2]))) - min(abs(int(e1[2])), abs(int(e2[2])))
                comparisons.add(str(x) + "," + str(y) + "," + str(z))
        cmpset.add(frozenset(comparisons))

    result = 0
    for s in cmpset:
        value = 0
        for e in s:
            for s1 in cmpset:
                if e in s1:
                    value += 1
                    break
        result += value/25
    
    print("Answer to part one: " + str(len(data) * len(data[0]) - int(result))) 

main()