from random import randint
from time import sleep


def print_board(board: list) -> None:
    c = 0
    for i in board:
        print(*i, sep=' | ')
        if c != 2:
            print('- - - - -')
            c += 1


def pk(board: list) -> list:
    print("Ходит пк")
    while True:
        n = randint(1, 9)
        if board[(n - 1) // 3][n % 3 - 1] != " ":
            continue
        board[(n - 1) // 3][n % 3 - 1] = "O"
        sleep(0.7)
        print_board(board)
        return board


def player():
    pass


def is_win(board: list) -> bool:
    if (board[0][0] == board[0][1] == board[0][2] != ' ') or (board[1][0] == board[1][1] == board[1][2] != ' ') or (board[2][0] == board[2][1] == board[2][2] != ' ') \
            or (board[0][0] == board[1][0] == board[2][0] != ' ') or (board[0][1] == board[1][1] == board[2][1] != ' ') or (board[0][2] == board[1][2] == board[2][2] != ' ') \
                or (board[0][0] == board[1][1] == board[2][2] != ' ') or (board[0][2] == board[1][1] == board[2][0] != ' '):
        return True
    return False


print_board([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

k = 0

while True:
    if (k % 2) == 0:
        n = input("Игрок, сделайте ход\t")
        if n == "стоп":
            break
        n = int(n)
        if not (1 <= n <= 9):
            print("Введите число от 1 до 9")
            continue
        if board[(n - 1) // 3][n % 3 - 1] != " ":
            print('Это поле уже занято')
            continue
        board[(n - 1) // 3][n % 3 - 1] = 'X'
        print_board(board)

    if (k % 2) == 1:
        board = pk(board)

    if is_win(board):
        print(("Поздравляю! Ты победил!", "Победа за компьютером!")[k % 2])
        break

    if sum([i.count(" ") for i in board]) == 0:
        print("Ничья")
        break

    k += 1
