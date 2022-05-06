def part_one(p1, p2):
    dice, turn = 0, False

    while p1[0] < 1000 and p2[0] < 1000:
        turn = not turn
        if turn: p = p1
        else: p = p2

        p[1] += sum([((ele % 100) + 1) for ele in range(dice, dice + 3)])
        p[0] += (p[1] % 10) + 1
        dice += 3

    return(min(p1[0], p2[0]) * dice)

def part_two(p1, p2):
    rolls = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                rolls.append(i+j+k)

    probable_rolls = {}
    for roll in rolls: 
        if roll not in probable_rolls.keys(): probable_rolls[roll] = rolls.count(roll)

    return max(quant_game([0, 0], p1, p2, True, probable_rolls, 1))

def quant_game(val, p1, p2, turn, rolls, dupes):
    if p1[0] >= 21: return [val[0] + dupes, val[1]]
    if p2[0] >= 21: return [val[0], val[1] + dupes]

    if turn:
        for key in rolls.keys():
            newp1 = [p1[0] + ((p1[1] + key) % 10) + 1, p1[1] + key]
            val = quant_game(val, newp1, p2, not turn, rolls, dupes * rolls[key])
    else: 
        for key in rolls.keys():
            newp2 = [p2[0] + ((p2[1] + key) % 10) + 1, p2[1] + key]
            val = quant_game(val, p1, newp2, not turn, rolls, dupes * rolls[key])

    return val

print("Answer to part one: {ans}".format(ans = part_one([0, 5 - 1], [0, 10 - 1])))
print("Answer to part two: {ans}".format(ans = part_two([0, 5 - 1], [0, 10 - 1])))