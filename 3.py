previous_num = -999999

while True:
    num = int(input('Введите число или 0 для остановки '))
    if num > previous_num and num != 0:
        previous_num = num
    if num == 0:
        break
print('Самое большое число в последовательности -', previous_num)
