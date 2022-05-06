def bingo():
    (numbers, boards) = get_data()
    winning_board = [[0, 0, 0], [0, 0, 0]]

    for board in boards:
        win = win_steps(board, numbers)
        if win[2] < winning_board[0][2] or winning_board[0][2] == 0: winning_board[0] = win
        if win[2] > winning_board[1][2]: winning_board[1] = win

    return [score_board(winning_board[0][0], winning_board[0][1]), score_board(winning_board[1][0], winning_board[1][1])]

def win_steps(board, numbers):
    win_con = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    steps = 0

    for i, row in enumerate(board):
        win_con.append(row)
        for j, ele in enumerate(row): win_con[j][i] = ele

    for number in numbers:
        steps += 1
        for con in win_con:
            if number in con:
                if len(con) == 1:
                    con.remove(number)
                    return (win_con, number, steps)
                else: con.remove(number)

def score_board(remain, number):
    result = 0

    for win_con in remain:
        for ele in win_con: result += int(ele)
    return int(result/2) * int(number)

def get_data():
    data = open("data.txt", "r").read().split("\n\n")
    numbers = data[0].split(",")
    data.remove(data[0])

    for i, board in enumerate(data):
        data[i] = board.split("\n")
        for j, row in enumerate(data[i]): data[i][j] = ' '.join(row.split(" ")).split()
    return(numbers, data)

print ("Answer to part one: " + str(bingo()[0]))
print ("Answer to part two: " + str(bingo()[1]))