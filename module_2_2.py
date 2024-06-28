first = 23
second = 50
third = 30

# Если все числа равны между собой, то вывести 3:
if first == second == third:
    # Или можно записать так: if first == second and first == third and second == third:
    print('Решение 1: ', 3)
else:
    print('Решение 1: Не верно')
print()

# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2:
if first == second or first == third or second == third:
    print('Решение 2: ', 2)
else:
    print('Решение 2: Не верно')
print()

# Если равных чисел среди 3-х вообще нет, то вывести 0:
if first != second or first != third or second != third:
    print('Решение 3: ', 0)
