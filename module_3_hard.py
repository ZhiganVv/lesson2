# Посчитать все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calc_sum_elements(*args):
    summa = 0
    for i in args:
        if isinstance(i, int):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, (tuple, list, set)):
            summa += calc_sum_elements(*i)
        elif isinstance(i, dict):
            summa += calc_sum_elements(*i.items())
    return summa


print(calc_sum_elements(data_structure))