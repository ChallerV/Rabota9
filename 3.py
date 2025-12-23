total_coins = 0  
amount_left = 0  
current_amount = 0 

current_amount = int(input("Введите сумму для оплаты ведьмаку: "))
amount_left = current_amount

while amount_left > 0:

    if amount_left >= 25:
        coins_25 = amount_left // 25
        total_coins += coins_25
        amount_left -= coins_25 * 25
        print(f"\nДобавлено {coins_25} монет(ы) по 25 чеканных монеты")

    elif amount_left >= 10:
        coins_10 = amount_left // 10
        total_coins += coins_10
        amount_left -= coins_10 * 10
        print(f"\nДобавлено {coins_10} монет(ы) по 10 крон")

    elif amount_left >= 5:
        coins_5 = amount_left // 5
        total_coins += coins_5
        amount_left -= coins_5 * 5
        print(f"\nДобавлено {coins_5} монет(ы) по 5 крон")

    else:
        coins_1 = amount_left
        total_coins += coins_1
        amount_left = 0
        print(f"\nДобавлено {coins_1} монет(ы) по 1 кроне")

    print(f"Текущий счётчик монет: {total_coins}, осталось оплатить: {amount_left}")

print(f"\nИтог: минимальное количество монет = {total_coins}")
