import random

for case in range(1, int(input()) + 1):
    for i in range(300):
        if i == 0:
            digits = 8
        else:
            digits = int(input())

        if digits == 0:
            break
        if digits == -1:
            break

        new = "00000000"
        indexList = [0, 1, 2, 3, 4, 5, 6, 7]
        random.shuffle(indexList)
        while new.count("1") < digits:
            index = indexList.pop()
            new = new[:index] + "1" + new[index + 1:]
        print(new)
    