cost = 0

while True:
    cost_ = int(input('Введите цену товара '))
    if cost_ < 0:
        print('Цена может быть только больше 0')
        continue
    elif cost_ == 0:
        break
    else:
        cost += cost_

if cost > 1000:
    cost = cost - 0.1 * cost
    print(f'Сумма товаров со скидкой 10%: {cost}')
else:
     print(f'Сумма товаров: {cost}')
