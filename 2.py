people_between = 0
current_name = "null"
past_name = "Александра"

print("Для определения количества людей  между Александрой и Левоном (если никого между ними нету, то введите <нет> или <Левон>):")

while current_name != "Левон":
    print(f"Введите имя следующего человека в очереди после {past_name}: ")
    current_name = input()

    if current_name == "Левон" or current_name == "нет":
        break
    
    elif current_name == "":
        people_between += 0
        print("Следующего человека в очереди нету\n")
    
    elif current_name == "Александра":
        print("Александра уже стоит в очереди (самая первая), её имя не может повторятся!\n")
        continue
    else:
        people_between += 1
        past_name = current_name
        continue


print(f"Количество людей между Александрой и Левоном = {people_between}")
