# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_fractional(num):
    for i in range(len(num)):
        s = num[i] // 1
        new.append(s)
        # print(new)
    for i in range(len(num)):
        q = num[i] - new[i]
        raz.append(round(q, 2))
        # print(raz)
    max = 0
    for i in range(len(raz)):
        last = raz[i]
        if last > max:
            max = last
            # print(max)
    min = max
    for i in range(len(raz)):
        last = raz[i]
        if last < min and last != 0:
            min = last
            # print(min)
    print(f'{num} => {max-min}')
   
num = [1.1, 1.2, 3.1, 5, 10.01]
# num = [1.31, 21.26, 3.87, 12, 10.3, 2.98]
new = []
raz = []
res = []
find_fractional(num)
