l = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
c = 0
for i in l:
    print(*i, sep=' | ')
    if c != 2:
        print('- - - - -')
        c += 1


lst = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
k = 0  # номер игрока
while True:
    n = input("Игрок номер {}, сделайте ход\t".format(k % 2 + 1))
         
    if n == "стоп":
        break
    
    n = int(n)
    
    if not (1 <= n <= 9):
        print("Введите число от 1 до 9")
        continue
    if lst[(n - 1) // 3][n % 3 - 1] != " ":
        print('Это поле уже занято')
        continue

    

    lst[(n - 1) // 3][n % 3 - 1] = ('X', 'O')[k % 2]

    c = 0
    for i in lst:
        print(*i, sep=' | ')
        if c != 2:
            print('- - - - -')
            c += 1

    if (lst[0][0] == lst[0][1] == lst[0][2] !=' ') or (lst[1][0] == lst[1][1] == lst[1][2] != ' ') or (lst[2][0] == lst[2][1] == lst[2][2] !=' ') \
        or (lst[0][0] == lst[1][0] == lst[2][0] != ' ') or (lst[0][1] == lst[1][1] == lst[2][1] !=' ') or (lst[0][2] == lst[1][2] == lst[2][2] != ' ') \
            or (lst[0][0] == lst[1][1] == lst[2][2] !=' ') or (lst[0][2] == lst[1][1] == lst[2][0] != ' '):
        print('Выиграл игрок {}!'.format(k % 2 + 1))
        break
    
    if sum([i.count(" ") for i in lst]) == 0:
        print("Ничья")
        break
    k += 1
