# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list_len = int(input('Введите количество элементов: '))
my_list = []
for i in range(list_len):
    my_list.append(round(random.uniform(1, 10), 3))
print(f'Изначальный список элементов: {my_list}')

def find_differ(sm_list):
    for i in range(len(sm_list)):
        sm_list[i] = abs(sm_list[i] - int(sm_list[i]))
    return round((max(sm_list) - min(sm_list)), 3)
print(f'Разница между максимальным и минимальным значением дробной части элементов {find_differ(my_list)}')

