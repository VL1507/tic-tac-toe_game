# крестики-нолики


def print_board(board: list) -> str:
    c = 0
    for i in board:
        print(*i, sep=' | ')
        if c != 2:
            print('- - - - -')
            c += 1


print_board([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
k = 0  # номер игрока

while True:
    n = input("Игрок номер {}, сделайте ход\t".format(k % 2 + 1))

    if n == "стоп":
        break

    n = int(n)

    if not (1 <= n <= 9):
        print("Введите число от 1 до 9")
        continue
    if board[(n - 1) // 3][n % 3 - 1] != " ":
        print('Это поле уже занято')
        continue

    board[(n - 1) // 3][n % 3 - 1] = ('X', 'O')[k % 2]

    print_board(board)

    if (board[0][0] == board[0][1] == board[0][2] != ' ') or (board[1][0] == board[1][1] == board[1][2] != ' ') or (board[2][0] == board[2][1] == board[2][2] != ' ') \
        or (board[0][0] == board[1][0] == board[2][0] != ' ') or (board[0][1] == board[1][1] == board[2][1] != ' ') or (board[0][2] == board[1][2] == board[2][2] != ' ') \
            or (board[0][0] == board[1][1] == board[2][2] != ' ') or (board[0][2] == board[1][1] == board[2][0] != ' '):
        print('Выиграл игрок {}!'.format(k % 2 + 1))
        break

    if sum([i.count(" ") for i in board]) == 0:
        print("Ничья")
        break
    k += 1
