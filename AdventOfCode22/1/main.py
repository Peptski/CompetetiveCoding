map = [0]
for line in open('./data').readlines():
    if line == '\n':
        map.append(0)
    else:
       map[-1] += int(line.strip())
        

print(f'Part one: {sorted(map)[-1]}')
print(f'Part two: {sum(sorted(map)[-3:])}')