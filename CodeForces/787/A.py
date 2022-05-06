for i in range(int(input())):
    data = [int(ele) for ele in input().split(" ")]
    dog = max(0, data[3] - data[0])
    cat = max(0, data[4] - data[1])
    ans = max(0, cat + dog - data[2])
    if ans > 0:
        print("NO")
    else:
        print("YES")