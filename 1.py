pin = 4590
while True:
    try_pin = int(input('Введите пинкод '))
    if try_pin == pin:
        print('Доступ разрешен')
        break
    else:
        print('Ошибка. Попробуйте еще раз')
