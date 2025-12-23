
num = int(input("Введите любое натуральное число: "))

three_count = 0 
last_digit_count = 0 # 
even_count = 0 
sum_big_five = 0 
product_big_seven = 1 
zero_five_count = 0 

last_d = num % 10

work_num = num

print(f"Последняя цифра: {last_d}")

digit_position = 1
while work_num > 0:
    current_d = work_num % 10

    print(f"Позиция {digit_position}: цифра {current_d}")

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

    work_num //= 10
    digit_position += 1
else:
    print(f"Всего проанализировано {digit_position - 1} цифр")

    if product_big_seven == 1:
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

print("\nРезультаты:")
print(three_count)
print(last_digit_count)
print(even_count)
print(sum_big_five)
print(product_big_seven)

print(zero_five_count)
