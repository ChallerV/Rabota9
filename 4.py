# Ввод числа
num = int(input("Введите любое натуральное число: "))

# Инициализация всех счётчиков
three_count = 0 # количество цифр 3 в нём
last_digit_count = 0 # сколько раз в нём встречается последняя цифра;
even_count = 0 # количество чётных цифр;
sum_big_five = 0 # сумма его цифр, больших пяти;
product_big_seven = 1 # произведение цифр, больших семи
zero_five_count = 0 # сколько раз в нём встречаются цифры 0 и 5

# Получаем последнюю цифру
last_d = num % 10

# Создаём временную переменную для обработки
work_num = num

print(f"Последняя цифра: {last_d}")

# Основной цикл с while-else
digit_position = 1
while work_num > 0:
    current_d = work_num % 10

    print(f"Позиция {digit_position}: цифра {current_d}")

    # Анализ текущей цифры
    if current_d == 3:
        three_count += 1

    if current_d == last_d:
        last_digit_count += 1

    if current_d % 2 == 0:
        even_count += 1

    if current_d > 5:
        sum_big_five += current_d

    if current_d > 7:
        product_big_seven *= current_d

    if current_d == 0 or current_d == 5:
        zero_five_count += 1

    # Подготовка к следующей итерации
    work_num //= 10
    digit_position += 1
else:
    # Этот блок выполнится после нормального завершения цикла
    print(f"Всего проанализировано {digit_position - 1} цифр")

    # Проверка особого случая для произведения
    if product_big_seven == 1:
        # Проверим, были ли цифры больше 7
        check_num = num
        gt7_found = False
        search_count = 0

        while check_num > 0:
            search_count += 1
            if check_num % 10 > 7:
                gt7_found = True
                break
            check_num //= 10

        if not gt7_found:
            product_big_seven = 1
            print("Цифр больше 7 не обнаружено")

# Вывод результатов
print("\nРезультаты:")
print(three_count)
print(last_digit_count)
print(even_count)
print(sum_big_five)
print(product_big_seven)
print(zero_five_count)