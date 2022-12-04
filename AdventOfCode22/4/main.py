data = open('./data').readlines()
totalOverlap = 0
anyOverlap = 0

for line in data:
    groups = [grp.split('-') for grp in line.strip().split(',')]
    if int(groups[0][0]) >= int(groups[1][0]) and int(groups[0][1]) <= int(groups[1][1]):
        totalOverlap += 1
    elif int(groups[1][0]) >= int(groups[0][0]) and int(groups[1][1]) <= int(groups[0][1]):
        totalOverlap += 1
    if not (int(groups[0][0]) > int(groups[1][1]) or int(groups[0][1]) < int(groups[1][0])):
        anyOverlap += 1

print(f'Part one: {totalOverlap}')
print(f'Part two: {anyOverlap}')
