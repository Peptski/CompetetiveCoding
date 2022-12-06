data = open('./data').readlines()[0]

def search(n):
    win = []
    pointer = 0
    count = 0
    for char in data:
        count += 1
        if len(win) < n:
            win.append(char)
        else:
            win[pointer] = char
            pointer = (pointer + 1) % n
        if len(set(win)) == n:
            print(f'Answer: {count}')
            break

search(4)
search(14)
