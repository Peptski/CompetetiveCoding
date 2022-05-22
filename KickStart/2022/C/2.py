for case in range(1, int(input()) + 1):
    num, x, y = [int(n) for n in input().split(" ")]

    sum = ((num*(num + 1))/2)
    div = (x + y)

    if sum % div == 0:
        print("Case #{}: {}".format(case, "POSSIBLE"))
        tot = int((sum // div) * x)
        nums = []
        for n in range(num, 0, -1):
            if n <= tot:
                nums.append(str(n))
                tot -= n
            if tot == 0:
                break

        print(len(nums))
        print(" ".join(nums))

    else:
        print("Case #{}: {}".format(case, "IMPOSSIBLE"))
    