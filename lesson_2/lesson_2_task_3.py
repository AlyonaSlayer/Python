import math
def square(square_side):
    square_area = square_side*square_side
    square_area = math.ceil(square_area)
    print("Площадь квадрата = ",square_area)  

square_side = float(input("Введите сторону квадрата "))
square(square_side)