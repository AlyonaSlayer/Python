def bank():
    x = float(input("Введите сумму вклада "))
    y = int(input ("Введите срок хранения "))
    for i in range(y+1):
        x = x+x/10
        print(i, x)
bank()