# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроенных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите число: '))
def binary_sys(number):
    bin_num = ''
    while number > 0:
        bin_num = str(number % 2) + bin_num
        number = number // 2
    return bin_num


print(f'Число {num} в двоичном коде -> {binary_sys(num)}')

