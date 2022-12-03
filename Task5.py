# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число: '))
def fibonacci(number):
    if number > 0:
        if number in [1, 2]:
            return 1
        else:
            return fibonacci(number - 1) + fibonacci(number - 2)
    else:
        if number == -1:
            return 1
        else:
            return fibonacci(number + 2) - fibonacci(number + 1)
my_list = [0]

for i in range(1, num + 1):
    my_list.append(fibonacci(i))
    my_list.insert(0, fibonacci(-i))
print(my_list)