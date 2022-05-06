import math

for case in range(1, int(input())+1):
    number = input()
    ans = ""
    start = min(math.floor(int(number + "0") // 9), 0)
    while len(str(start * 9)) - 1 <= len(number):
        if len(str(start * 9)) - 1 == len(number):
            val = str(start * 9)
            errors = 0
            for i in range(len(number)):
                if number[i] != val[i + errors]:
                    errors += 1
                    if errors == 1:
                        if number[i] != val[i + errors]:
                            errors += 1
                if errors > 1:
                    break
            if errors <= 1:
                ans = val
                print("Case #{}: {}".format(case, ans))
                break
        start += 1
    if ans == "": 
        print("Case #{}: IMPOSSIBLE".format(case))