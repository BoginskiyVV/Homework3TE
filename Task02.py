# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем
# первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def mult(num):
    size = len(num)
    ind = len(num) - 1
    if size % 2 == 0:
        elem = (size // 2)
    else:
        elem = (size // 2) + 1
    count = 0
    for i in range(0, len(num)):
        if count < elem and i <= size:
            x = num[i]
            y = num[ind]
            z = x * y
            new.append(z)
        i += 1
        ind -= 1
        count += 1
    print(new)

# num = [2, 3, 5, 6]
# num = [2, 3, 4, 5, 6]
# num = [2, 8, 6, 4, 7, 3, 1, 9]
num = [3, 7, 9, 4, 5, 6, 2]
new = []
mult(num)

