n = int(input("Введите натуральное число n: \n"))

current_number = 1

print(f"Натуральные числа от 1 до {n} (за исключением заданных диапазонов):")

while current_number <= n:
    if 5 <= current_number <= 9:
        current_number += 1
        continue

    if 17 <= current_number <= 37:
        current_number += 1
        continue

    if 78 <= current_number <= 87:
        current_number += 1
        continue

    print(f"{current_number}", end=" ")

    current_number += 1