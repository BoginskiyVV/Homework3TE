# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def con_bynary(x):
    while x > 0:
        last = x % 2
        # print(last)
        q.append(last)
        x = x // 2

x = int(input('Для преобразования введите число: '))
q = []

con_bynary(x)
t = q[::-1]

res = int(str(t).replace(' ', '').replace('[', '').replace(']', '').replace(',', ''))
print(f'{x} -> {res}')