# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

sum = int(input('Введите сумму чисел: '))
product = int(input('Введите произведение чисел: '))
c = 0
for x in range (0, 1000):
    if c: break
    for y in range (0, 1000):
        if x + y == sum and x * y == product:
            c = 1
            print(x)
            print(y)
            break
else:
    print('Петя не верно подсчитал числа, надо заново пересчитать. ') 