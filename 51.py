# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def power(number, degree):
    if (degree == 1):
        return (number) 
    if (degree != 1):
        return (number * power(number, degree - 1))
number = int(input("Введите любое число: "))
degree = int(input("Введите его степень: "))
print("Результат возведения числа в степень равен:", power(number, degree))
