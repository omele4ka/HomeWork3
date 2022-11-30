# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

list_len = int(input('Введите количество элементов: '))
my_list = []
for i in range(1, list_len + 1):
    my_list.append(random.randint(1, 100))
print(f'Исходный список элементов: {my_list}')

def sum_odd_elem(list):
    count = 0
    for i in range(1, len(list), 2):
        count += list[i]
    return count
print(f'Сумма элементов, стоящих на нечетной позиции равна {sum_odd_elem(my_list)}')




