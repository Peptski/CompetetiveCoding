storage1 = [["L", "N", "W", "T", "D"], ["C", "P", "H"], ["W", "P", "H", "N", "D", "G", "M", "J"], ["C", "W", "S", "N", "T", "Q", "L"], ["P", "H", "C", "N"], ["T", "H", "N", "D", "M", "W", "Q", "B", ], ["M","B", "R", "J", "G", "S", "L"], ["Z", "N", "W", "G", "V", "B", "R", "T"], ["W", "G", "D", "N", "P", "L"]]
storage2 = [["L", "N", "W", "T", "D"], ["C", "P", "H"], ["W", "P", "H", "N", "D", "G", "M", "J"], ["C", "W", "S", "N", "T", "Q", "L"], ["P", "H", "C", "N"], ["T", "H", "N", "D", "M", "W", "Q", "B", ], ["M","B", "R", "J", "G", "S", "L"], ["Z", "N", "W", "G", "V", "B", "R", "T"], ["W", "G", "D", "N", "P", "L"]]

def move(n, origin, dest):
    for i in range(n):
        storage1[dest].append(storage1[origin][-1])
        storage1[origin].pop()

def move_several(n, origin, dest):
    storage2[dest] += storage2[origin][-n:]
    for i in range(n):
        storage2[origin].pop()

def done():
    for i in range(len(storage1)):
        storage1[i] = storage1[i][-1]
        storage2[i] = storage2[i][-1]

    print(f'Part one: {storage1}')
    print(f'Part two: {storage2}')

for line in open('./data').readlines():
    data = line.strip().split(" ")
    move(int(data[1]), int(data[3]) - 1, int(data[5]) - 1) 
    move_several(int(data[1]), int(data[3]) - 1, int(data[5]) - 1)
done()
