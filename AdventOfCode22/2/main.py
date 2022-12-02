totalOne, totalTwo = 0, 0
for move, response in [[ord(line[0]) - ord('A'), ord(line.strip()[-1]) - ord('X')] for line in open('data').readlines()]:
    if move == response: totalOne += 3 
    if (move + 1) % 3 == response: totalOne += 6
    totalOne += response + 1

    match response:
        case 0: totalTwo += (move - 1) % 3 + 1
        case 1: totalTwo += move + 3 + 1
        case 2: totalTwo += (move + 1) % 3 + 6 + 1

print(f'Part one: {totalOne}')
print(f'Part two: {totalTwo}')
