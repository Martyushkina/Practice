def check_triangle(a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    else:
        return False
    
try:
    a = float(input("Введите первую сторону треугольника: "))
    b = float(input("Введите вторую сторону треугольника: "))
    c = float(input("Введите третью сторону треугольника: "))
    exist = check_triangle(a, b, c)
    
    if exist:
        if a == b and a == c:
            print("Треугольник правильный")

        elif a == b or b == c or a == c:
            print("Треугольник равобедренный")
            
        else:
            if a ** 2 + b ** 2 == c ** 2 or c ** 2 + b ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
                print("Треугольник прямоугольный")
            else:
                print("Треугольник не является ни правильным, ни равнобедренным, ни прямоугольным")

    else:
        print("Треугольника с введёнными сторонами не существует")
        
except ValueError:
    print("Вы ввели неправильные данные. Скорее всего, вы ввели строку.\nПопробуйте ввести числа заново ")


    


    
