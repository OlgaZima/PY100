print('XXXXXXXXXXXXXXXX    КРЕСТИКИ НОЛИКИ    0000000000000000')


row = col = 3  # матрица 3x3

# создание игрового поля (двумерный массив)
def gen_desk(col=3) -> list:
    desk = [[0] * col for k in range(col)]  # генерация двумерного списка
    for i in range(col):
        for j in range(col):
            desk[i][j] = int(str(i + 1) + str(j + 1))
    return desk


# отрисовка игрового поля
def draw_table(desk: list, row: int = 3) -> None:
    for i in range(row):
        print('--------------')
        for j in range(row):
            print(desk[i][j], end=' | ')
        print()
    print('--------------')


# сгенерируем выигрышные линии (в линиях будут значения матрицы), col * 2 + 2
def win_(desk: list, col=3) -> list:
    win_row = [[0] * col for k in range(col)]  # генерация двумерного списка для строчек
    win_col = [[0] * col for k in range(col)]  # генерация двумерного списка для столбцов
    win_diag_m = [[0] * col for k in range(1)]  # генерация двумерного списка для диагоналей
    win_diag_u = [[0] * col for k in range(1)]
    for i in range(len(desk)):
        for j in range(len(desk)):
            win_row[i][j] = desk[i][j]
    for i in range(len(desk)):
        for j in range(len(desk)):
            win_col[j][i] = desk[i][j]
    for i in range(len(desk)):
        for j in range(len(desk)):
            if i == j:
                win_diag_m[0][j] = desk[i][j]
    for i in range(len(desk)):
        for j in range(len(desk)):
            if j == col - 1 - i:
                win_diag_u[0][j] = desk[i][j]
    win = win_row + win_col + win_diag_m + win_diag_u
    return win


# Ходы, X or 0 не выбираем, только номер ячейки
# Ф-ция изменяет desk (игровое поле) и win (выигрышные линии),записываются X or 0
def input_(desk: list, win: list, count: int):
    if count % 2 == 0:
        symbol = 'X'
        step = input('Сделайте ваш ход (например 22, если свободно), исходя из ситуации на доске__')
    elif count % 2 != 0:
        symbol = '0'
        step = input('Сделайте ваш ход (например 13, если свободно), исходя из ситуации на доске__')
    if step.isdigit():
        for i in range(len(desk)):
            for j in range(len(desk)):
                if desk[i][j] == int(step):
                    desk[i][j] = symbol
                    count += 1
                    for w in range(len(win)):
                        for w_ in range(col):
                            if win[w][w_] == int(step):
                                win[w][w_] = symbol
    else:
        print('                Повторите ввод, двузначное число, как правило!!!')
        return desk, win, count

    return desk, win, count


# проверка выигрыша
def win_check(win: list, col=3):
    for i in range(len(win)):
        count_X = 0
        count_0 = 0
        for j in range(col):
            if win[i][j] == 'X':
                count_X += 1
                if count_X == col:
                    return count_X, count_0
            elif win[i][j] == '0':
                count_0 += 1
                if count_0 == col:
                    return count_0, count_X
    return count_X, count_0


def main():
    gen_desk(col=3)
    desk = gen_desk(col=3)
    win_(desk, col=3)
    draw_table(desk, row=3)
    count = 0
    while True:
        win = win_(desk, col)
        desk, win, count1 = input_(desk, win, count)
        if count1 == count:
            print('                     Ячейка занята, повторите ввод!!!')
        else:
            count = count1
        count_X, count_0 = win_check(win, col=3)
        draw_table(desk, row=3)
        if count_X == col:
            print('Выиграли крестики!')
            break
        if count_0 == col:
            print('Выиграли нолики!')
            break
        if count == col * row:
            print('Ничья!')
            break


if __name__ == "__main__":
    main()




