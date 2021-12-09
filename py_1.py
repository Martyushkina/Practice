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
            
        if a ** 2 + b ** 2 == c ** 2 or c ** 2 + b ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
            print("Треугольник прямоугольный")
        else:
            if max(a, b, c) == b:
                max_side = b
                b = a
                a = max_side
            elif max(a, b, c) == c:
                max_side = c
                c = a
                a = max_side
                    
            cos = (b ** 2 + c ** 2 - a ** 2)//(2 * b * c)

            if cos < 0:
                print("Треугольник тупоугольный")
            else:
                print("Треугольник остроугольный")
            

    else:
        print("Треугольника с введёнными сторонами не существует")
        
except ValueError:
    print("Вы ввели неправильные данные. Скорее всего, вы ввели строку.\nПопробуйте ввести числа заново ")


    


    
