scoreOne, scoreTwo = 0, 0
shared = {}
mode = 0

for line in [line.strip() for line in open('./data').readlines()]:
    
    if mode == 0:
        shared = set(list(line))
    else:
        shared = shared.intersection(set(list(line))) 

    if mode == 2: 
        for char in shared:
            if ord(char) >= ord('a'):
                scoreTwo += ord(char) - ord('a') + 1
            else:
                scoreTwo += ord(char) - ord('A') + 27

    for char in set(list(line[:len(line)//2])).intersection(set(list(line[len(line)//2:]))):
        if ord(char) >= ord('a'):
            scoreOne += ord(char) - ord('a') + 1
        else:
            scoreOne += ord(char) - ord('A') + 27

    mode = (mode + 1) % 3

print(f'Part one: {scoreOne}')
print(f'Part two: {scoreTwo}')