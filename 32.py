# 3.2[18]: Требуется найти в списке целых чисел самый близкий по 
# величине элемент к заданному числу X. Пользователь вводит это число с клавиатуры, 
# список можно считать заданным. Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

n = int(input("Введите размер массива "))
list_1 = list()
for i in range(n):
    x = int(input("Введите элементы массива "))
    list_1.append(x)

k = int(input("Введите число, которе будет сравниваться с элементами массива "))
m = abs(k - list_1[0]) 

number = list_1[0]
for i in range(1, len(list_1)):
    if m >= abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(f' Ближайшее число к элементу из массива {k} - {number}')
