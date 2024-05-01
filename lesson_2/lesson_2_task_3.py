def square():
    a = input("Введите сторону квадрата")
    x = round(a,1)
    if x > a:
        y = x*x
        print(y)
    elif x < a:
        x = x+1
        y = x*x
        print(y)
    elif x == a:
        y = x*x
        print(y)
    

square() 