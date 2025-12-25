amount = 1000
while True:
    print('''1. Узнать баланс
2. Снять 100 руб
3. Положить 100 руб
4. Выход''')
    command = input('Введите номер операции ')
    if command == '1':
        print('Ваш баланс : ', amount)
        print('==============================')
        continue
    elif command == '2':
        if amount >= 100:
            amount -= 100
            print('Снято 100 руб')
            print('==============================')
            continue
        else:
            print('Недостаточно средств ')
            print('==============================')
    elif command == '3':
        amount += 100
        print('Пополено 100 руб')
        print('==============================')
        continue
    elif command == '4':
        print('До свидания')
        break
    else:
        print('Введена неправильная команда')
