from typing import List, Tuple


def gen_desk(col: int) -> List[list]:
    """
    Ф-ция генеририует двумерный список, кол-во вложенных списков (col) = кол-ву элементов (col) во вложенном списке
    :param col: int, кол-во столбцов = кол-во строк (row)
    :return: List[list], где list[int], двумерный список, где длина = row, кол-во элементов = col * row
    """
    desk = []
    for i in range(col):
        row = []
        for j in range(col):
            row.append(int(str(i + 1) + str(j + 1)))
        desk.append(row)
    return desk


def draw_table(desk: List[list], col: int) -> None:
    """
    Ф-ция рисует квадртное игровое поле размера col (кол-во столбцов) x row (кол-во строк) в консоли
    :param desk: List[list], двумерный список, где длина = row, кол-во элементов = col * row
    :param col: int, кол-во столбцов
    :return: None, рисует квадратное игровое поле в консоли
    """
    for i in range(col):
        print('--------------')
        for j in range(col):
            print(desk[i][j], end=' | ')
        print()
    print('--------------')


def get_win_lines(desk: List[list], row: int) -> List[list]:
    """
    Ф-ция создает двумерный список, содержащий выигрышные линии, кол-во которых = row * 2 + 2
    :param desk: List[list], двумерный список, где длина = row, кол-во элементов = col * row
    :param row: int (row = col), кол-во строк
    :return: List[list], двумерный список, где длина = row * 2 + 2
    """
    win_row = [[0] * row for k in range(row)]  # пустой список
    win_col = [[0] * row for k in range(row)]  # -//-
    win_diag_m = [[0] * row]  # -//-
    win_diag_u = [[0] * row]  # -//-
    for i in range(row):
        for j in range(row):
            win_row[i][j] = desk[i][j]  # горизонталь
            win_col[j][i] = desk[i][j]  # вертикаль
            if i == j:
                win_diag_m[0][j] = desk[i][j]  # главная диагональ (i = j)
            if j == row - 1 - i:
                win_diag_u[0][j] = desk[i][j]  # побочная диагональ (i + j = row - 1)
    win = win_row + win_col + win_diag_m + win_diag_u
    return win


def input_X0(col: int) -> int and int:
    """
    Ф-ция позволяет выбрать символ X/0 для 1-го хода/игрока
    :param col: int кол-во столбцов = row
    :return: возвращает count - идентификатор 1-го хода; count_max - max кол-во правильных ходов
    """
    while True:
        symbol = input('Выберите символ, которым будете играть X или 0 __')
        sym = ('X', '0')
        if symbol.upper() not in sym:
            print('X - латинская буква, 0 - цифра, повторите ввод__')
        else:
            count = 0
            count_max = col * col
            if symbol == '0':
                count = 1
                count_max += 1
            break
    return count, count_max


def input_(desk: List[list], win: List[list], count: int) -> Tuple[int, List[list], List[list]]:
    """
    Ф-ция, которая записывает символы 'X/0' в игровой список и список выигрышных линий и счетчик ходов
    :param desk: List[list], ф-ция записывает 'X/0' в игровой список
    :param win: List[list], ф-ция записывает 'X/0' в список выигрышных линий
    :param count: int, счеткчик ходов
    :return: desk, win, count
    """
    if count % 2 == 0:
        symbol = 'X'
        step = input('Введите позицию для X (например 22), исходя из ситуации на доске__')
    elif count % 2 != 0:
        symbol = '0'
        step = input('Введите позицию для 0 (например 13), исходя из ситуации на доске__')
    if step.isdigit():
        try:
            i, j = int(step[0]), int(step[1])  # if i - 1 and j - 1, as a result index for ceil
            print(i, j)
            if desk[i - 1][j - 1] not in ('X', '0'):
                desk[i - 1][j - 1] = symbol
                count += 1
        except Exception:
            print('                Повторите ввод, выбрав свободную ячейку!!!')
            return desk, win, count
        for i1, row in enumerate(win):
            for j1, ceil in enumerate(row):
                if ceil == int(step[0] + step[1]):
                    win[i1][j1] = symbol
    else:
        print('                Повторите ввод, вы ввели не цифры!!!')
        return desk, win, count

    return desk, win, count


def win_check(win: List[list], col: int) -> int and str:
    """
    Ф-ция проверяет кол-во символов 'X/0' в выигрышных линниях
    :param win: List[list], список выигрышных линий
    :param col: int, кол-во столбцов
    :return: int - 3/0 - выиграли/ничья; str - кто выиграл or None - ничья
    """
    for line in win:
        count_X = 0
        count_0 = 0
        for ceil in line:
            if ceil == 'X':
                count_X += 1
            elif ceil == '0':
                count_0 += 1
        if count_X == col:
            return count_X, 'крестики'
        if count_0 == col:
            return count_0, 'нолики'
    return 0, None


def game(col: int, row: int):
    """
    Ф-ция одной партии игры, возвращает результат игры
    :return: печатает результат игры в консоли
    """
    desk = gen_desk(col=col)
    draw_table(desk, col=col)
    win = get_win_lines(desk, row)
    count, count_max = input_X0(col)
    while True:
        desk, win, count1 = input_(desk, win, count)
        if count1 == count:
            print('                     Ячейка занята/отсутствует, повторите ввод!!!')
            continue
        count = count1
        count_sequence, player = win_check(win, col=col)
        draw_table(desk, col=col)
        if count_sequence == col:
            print(f'Выиграли {player}!')
            break
        if count == count_max:
            print('Ничья!')
            break


def main():
    """
    Основаня ф-ция игры, которая ведет диалог с пользователем: запрашивает размер поля, запускает партию игры
    :return:
    """
    while True:
        print('')
        size = (input('Выберите размер поля N x N, где 3 =< N <= 9__'))
        try:
            if int(size) not in (list(range(3, 10))):
                print('Размер поля от 3 до 9, повторите ввод__')
            else:
                col = row = int(size)
        except Exception:
            print('Введите цифру от 3 до 9, повторите ввод__')
        game(col, row)
        print('')
        new_game = input('Продолжить играть? Если нет, то введите N__')
        if new_game.upper() == 'N' and len(new_game) == 1:
            break

if __name__ == "__main__":
    print('XXXXXXXXXXXXXXXX    КРЕСТИКИ НОЛИКИ    0000000000000000')
    main()