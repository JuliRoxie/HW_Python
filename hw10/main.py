'''
Гипотеза Коллатца
может быть кратко выражена следующим образом:

берём любое натуральное число n, если оно чётное,
то делим его на 2 если нечётное, то умножаем на 3
и прибавляем 1 (получаем 3n + 1) над полученным
числом выполняем те же самые действия, и так далее.

Гипотеза Коллатца заключается в том, что какое бы
начальное число n мы ни взяли, рано или поздно мы
получим единицу.

Пример
Для числа 12:
12
6
3
10
5
16
8
4
2
1
Всего получаем 9 шагов.

Задача
Вычислить число шагов для числа n, согласно гипотезе
Коллатца необходимых для достижения этим числом единицы.
'''


def schet(name):
    name = int(name)
    i = 0
    while name != 1:
        i += 1
        if name % 2 == 0:
            name /= 2
        else:
            name = name*3 + 1
    return i


inp = input()
if inp.isdigit():
    print(schet(inp))
else:
    print("Это не число!")
