# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

import random

list_len = int(input('Введите количество элементов: '))
my_list = []
for i in range(1, list_len + 1):
    my_list.append(random.randint(1, 10))
print(f'Исходный список элементов: {my_list}')

def multiply_pair(list):
    res_list = []
    if len(list) % 2 == 0:
        for i in range(len(list) // 2):
            res_list.append(list[i] * list[-(1 + i)])
    else:
        for i in range(len(list) // 2 + 1):
            res_list.append(list[i] * list[-(1 + i)])
    return res_list


print(f'Произведение пар чисел равно: {multiply_pair(my_list)}')

