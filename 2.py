num_1 = int(input('Введите первое число '))

while True:
    num_2 = int(input('Введите второе число '))
    if num_2 > num_1:
        break
    else:
        print('Введите число больше ', num_1)
while True:
    num_3 = int(input('Введите третье число '))
    if num_3 > num_2:
        break
    else:
        print('Введите число большее ', num_2)
print('Последовательность принята')
