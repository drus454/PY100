import random

def print_field(field):
    for row in field:
        print('|', end='')
        for cell in row:
            if cell is None:
                print(' |', end='')
            else:
                print(f'{cell}|', end='')
        print()

def is_win(field: list[list]):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] and field[i][0] is not None:
            print(f'Выиграл этот пользователь {field[i][0]}')
            return True
        if field[0][i] == field[1][i] == field[2][i] and field[0][i] is not None:
            print(f'Выиграл этот пользователь {field[0][i]}')
            return True
    # Проверка диагоналей
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] is not None:
        print(f'Выиграл этот пользователь {field[0][0]}')
        return True
    if field[0][2] == field[1][1] == field[2][0] and field[0][2] is not None:
        print(f'Выиграл этот пользователь {field[0][2]}')
        return True
    return False

def move():
    while True:
        try:
            row = int(input('Куда будешь ставить(строка): '))
            col = int(input('Куда будешь ставить(столбец): '))
            return row, col
        except ValueError:
            print('Ошибка нужно только целое число')

def main():
    field = [[None, None, None],
             [None, None, None],
             [None, None, None]
             ]

    is_first = input('Будешь ходить первым? [y/n]: ')
    symb = input('Выбери символ [x/o]: ')

    if is_first == 'y':
        player = symb
        current_player = 'h'
    else:
        player = 'x' if symb == 'o' else 'o'
        current_player = 'c'

    print('Вот начало игры. Любуйся пустым полем')
    print_field(field)

    for i in range(9):
        if current_player == 'h':
            while True:
                row, col = move()
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if field[row][col] is None:
                        break
                    else:
                        print('Ошибка: ячейка уже занята')
                else:
                    print('Ошибка: неверный диапазон')
            field[row][col] = player
        else:
            print('Ход компьютера')
            while True:
                col, row = random.randint(0, 2), random.randint(0, 2)
                if field[row][col] is None:
                    break
            field[row][col] = player
        print_field(field)

        winner = is_win(field)
        if winner:
            break

        player = 'x' if player == 'o' else 'o'
        current_player = 'c' if current_player == 'h' else 'h'
    if not winner:
        print('Ничья!!!')

if __name__ == '__main__':
    main()



