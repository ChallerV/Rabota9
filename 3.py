total_coins = 0  # Общее количество монет
amount_left = 0  # Оставшаяся сумма
current_amount = 0  # Текущая сумма для обработки

current_amount = int(input("Введите сумму для оплаты ведьмаку: "))
amount_left = current_amount

while amount_left > 0:

    # Проверяем самый крупный номинал - 25
    if amount_left >= 25:
        coins_25 = amount_left // 25
        total_coins += coins_25
        amount_left -= coins_25 * 25
        print(f"\nДобавлено {coins_25} монет(ы) по 25 чеканных монеты")

    # Проверяем номинал 10
    elif amount_left >= 10:
        coins_10 = amount_left // 10
        total_coins += coins_10
        amount_left -= coins_10 * 10
        print(f"\nДобавлено {coins_10} монет(ы) по 10 крон")

    # Проверяем номинал 5
    elif amount_left >= 5:
        coins_5 = amount_left // 5
        total_coins += coins_5
        amount_left -= coins_5 * 5
        print(f"\nДобавлено {coins_5} монет(ы) по 5 крон")

    # Остаток оплачиваем монетами по 1
    else:
        coins_1 = amount_left
        total_coins += coins_1
        amount_left = 0
        print(f"\nДобавлено {coins_1} монет(ы) по 1 кроне")

    # Вывод промежуточного состояния
    print(f"Текущий счётчик монет: {total_coins}, осталось оплатить: {amount_left}")

print(f"\nИтог: минимальное количество монет = {total_coins}")