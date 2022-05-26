import keyboard

COLORS = [i + 31 for i in range(5)] * 4


def input_params_and_start_alg():
    time_variable = 6
    while True:
        disks = input('Введите количество дисков от 3 до 20: ')
        try:
            if not (20 >= int(disks) >= 3):
                raise
        except(Exception,):
            print('Введены неправильные данные')
            continue
        break
    while True:
        towers = input('Введите количество башен от 3 до 10: ')
        try:
            if not (10 >= int(towers) >= 3):
                raise
        except(Exception,):
            print('Введены неправильные данные')
            continue
        break
    while True:
        start_t = input('Введите номер начальной башни: ')
        try:
            if not (int(towers) >= int(start_t) >= 1):
                raise
        except(Exception,):
            print('Введены неправильные данные ')
            continue
        break
    while True:
        finish_t = input('Введите номер конечной башни: ')
        try:
            if not (int(towers) >= int(finish_t) >= 1 and int(finish_t) != int(start_t)):
                raise
        except(Exception,):
            print('Введены неправильные данные ')
            continue
        break
    while True:
        temp = time_variable - int(start_t) - int(finish_t)
        if temp <= 0 or temp == int(start_t) or temp == int(finish_t):
            time_variable += 1
        else:
            break
    towers = generate_start_towers(int(disks), int(towers), int(start_t))
    hanoi_algorithm(int(disks), int(start_t), int(finish_t), towers, time_variable, int(disks))


def generate_start_towers(n_disks, n_towers, start):
    towers = [[] for _ in range(n_towers)]
    towers[start - 1] = [i + 1 for i in reversed(range(n_disks))]
    print_towers(towers, n_disks)
    return towers


def hanoi_algorithm(n, start, finish, towers, temporary_variable, count_disks):
    if n <= 0:
        return
    temp = temporary_variable - start - finish
    hanoi_algorithm(n - 1, start, temp, towers, temporary_variable, count_disks)
    towers[finish - 1].append(towers[start - 1][-1])
    towers[start - 1].pop(-1)
    print_towers(towers, count_disks)
    hanoi_algorithm(n - 1, temp, finish, towers, temporary_variable, count_disks)


def print_towers(towers, count_disks):
    for i in reversed(range(count_disks)):
        for j in range(len(towers)):
            try:
                color_code = f'\033[{COLORS[towers[j][i] - 1]}m ' + '{:^3}'
                print(color_code.format(towers[j][i]), end='')
            except IndexError:
                print('\033[37m {:^3}'.format('|'), end='')
        print()
    print()
    keyboard.wait("Enter")


if __name__ == '__main__':
    input_params_and_start_alg()
