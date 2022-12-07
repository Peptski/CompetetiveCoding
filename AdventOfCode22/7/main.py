path = []
dirs = {}

for line in [line.strip() for line in open('./data').readlines()]:
    if line[:3] == '$ c':
        newDir = line.split(' ')[2]
        if newDir == '..':
            path.pop()
        elif newDir == '/':
            path = ['/']
        else:
            path.append(newDir)

    elif line[0] != 'd' and line[0] != '$':
        size = int(line.split(' ')[0])
        for index, dir in enumerate(path):
            dirs["/".join(path[:index + 1])] = dirs.setdefault("/".join(path[:index + 1]), 0) + size

sum = 0
for val in dirs.values():
    if val <= 100000:
        sum += val
print(f'Part one: {sum}')

target = 30000000 - (70000000 - dirs['/'])
min = 30000000
for val in dirs.values():
    if val > target and val < min:
        min = val
print(f'Part two: {min}')
