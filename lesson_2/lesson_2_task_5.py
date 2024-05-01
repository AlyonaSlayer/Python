def month_to_season():
    num = int(input("Введите номер месяца "))
    if num == 1:
        print("Зима")
    elif num == 2:
        print("Зима")
    elif num == 3:
        print("Весна")
    elif num == 4:
        print("Весна")
    elif num == 5:
        print("Весна")
    elif num == 6:
        print("Лето")
    elif num == 7:
        print("Лето")
    elif num == 8:
        print("Лето")
    elif num == 9:
        print("Осень")
    elif num == 10:
        print("Осень")
    elif num == 11:
        print("Осень")
    elif num == 12:
        print("Зима")
    else: 
        print("В году 12 месяцев, пожалуйста введите число от 1 до 12!")
        month_to_season()

month_to_season()