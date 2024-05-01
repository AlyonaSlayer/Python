def is_year_lip(year):
    if (year % 4 == 0):
        x = True
        print("год",year,":",x)
    else:
        y = False
        print("год",year,":",y)

year = int(input("Введите год: "))
is_year_lip(year)
