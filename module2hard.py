while True:
    field_one = list(range(3, 21))
    number = list(range(1, 21))
    number_obt = int(input(f'Введите число на первом камне: '))
    field_two = []
    if number_obt in field_one:
        for i in range(1, number_obt + 1):
            for j in range(1, number_obt + 1):
                if i != j and number_obt % (i + j) == 0 and i < j:
                    field_two.append(str(i) + str(j))
                    continue
    else:
        print('Число не верное')
    print(''.join(field_two))