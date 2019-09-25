games = [
    [
        ['X', 'X', 'O'],
        ['O', 'X', 'O'],
        ['O', 'O', 'X']
    ],
    [
        ['O', 'O', 'O'],
        ['X', 'X', 'O'],
        ['O', 'O', 'X']
    ],
    [
        ['X', 'X', 'O'],
        ['X', 'O', 'O'],
        ['X', 'O', 'X']
    ]
]


def getWinner(board):
    columns = [[], [], []]

    # check rows
    for row in board:
        columns[0].append(row[0])
        columns[1].append(row[1])
        columns[2].append(row[2])

        if row[0] == row[1] == row[2]:
            return row[0]

    # check columns
    for row in columns:
        if row[0] == row[1] == row[2]:
            return row[0]

    # check diagonals
    if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
        return board[1][1]

    # no winner
    return None


for game in games:
    print("The winner is %s's" % (getWinner(game)))
