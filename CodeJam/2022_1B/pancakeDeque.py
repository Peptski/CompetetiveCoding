for case in range(1, int(input()) + 1):
    lp = 0
    maxPay = 0
    last = 0
    rp = int(input()) - 1
    listOfPancakes = [int(val) for val in input().split(" ")]
    while lp <= rp:
        if last > listOfPancakes[lp] and last > listOfPancakes[rp]: 
            lp += 1
            rp -= 1
        else:
            if listOfPancakes[lp] <= listOfPancakes[rp]:
                if listOfPancakes[lp] >= last:
                    last = listOfPancakes[lp]
                    maxPay += 1
                lp += 1
            else:
                if listOfPancakes[rp] >= last:
                    last = listOfPancakes[rp]
                    maxPay += 1
                rp -= 1
    print("Case #{}: {}".format(case, maxPay))