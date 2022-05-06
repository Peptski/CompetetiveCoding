for i in range(int(input())):
    nums = int(input())
    numList = [int(num) for num in input().split(" ")]
    count = 0
    current = 0
    last = numList[-1] + 1
    for element in reversed(numList):
        if last == 0:
            print(-1)
            break

        current = element
        if element >= last:
            while current >= last:
                current = int(current / 2)
                count += 1
        last = current
    else:
        print(count)
