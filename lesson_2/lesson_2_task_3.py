def square():
    a = float(input("Введите сторону квадрата"))
    x = round(a)
    if x > a:
        y = x*x
        print(y)
    elif x < a:
        x = x+1
        y = x*x
        print(y)
    elif x == a:
        y = x*x
        print("Площадь квадрата = ",y)
    

square()