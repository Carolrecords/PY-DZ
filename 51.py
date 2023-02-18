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
    elif (degree != 1):
        return (number * power(number, degree - 1))
number = int(input("Введите любое число: "))
degree = int(input("Введите его степень: "))
print("Результат возведения числа в степень равен:", power(number, degree))

# ______________________________________________________________________________________
# Решения отличные)
# В задаче 51 код:

# if (degree == 1):
# return (number)
# if (degree != 1):
# return (number * power(number, degree - 1))

# # лучше реализовывать или через elif

# if (degree == 1):
# return (number)
# elif (degree != 1):
# return (number * power(number, degree - 1))

# или else:

# if (degree == 1):
# return (number)
# else:
# return (number * power(number, degree - 1))

# Cтарайтесь вместо набора if использовать связку if elif else. Почему? 
# Если у нас будет набор условий взаимоисключающих, то при куче if они все могу выполниться, 
# а переход к elif происходит только если не выполнилось предыдущее значение. 
# Например:

# age = 18
# if age < 14:
# print("Ты несовершеннолетний")
# elif age < 18:
# print("ДА у тебя уже есть паспорт")
# elif age < 21:
# print("Паспорт есть, но крепкий алкоголь тебе не продадим")
# else:
# print("Всё дозволено")

# попробуйте исполнить код и сравнить с решением:

# age = 18
# if age < 14:
# print("Ты несовершеннолетний")
# if age < 18:
# print("ДА у тебя уже есть паспорт")
# if age < 21:
# print("Паспорт есть, но крепкий алкоголь тебе не продадим")
# else:
# print("Всё дозволено")