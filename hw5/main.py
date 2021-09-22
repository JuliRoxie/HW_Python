'''
Встроенная функция input позволяет ожидать и возвращать данные из стандартного
ввода ввиде строки (весь введенный пользователем текст до нажатия им enter).
Используя данную функцию, напишите программу, которая:

1. После запуска предлагает пользователю ввести неотрицательные целые числа,
разделенные через пробел и ожидает ввода от пользователя.
2. Находит наименьшее положительное число, не входящее в данный пользователем
список чисел и печатает его.

Например:

-> 2 1 8 4 2 3 5 7 10 18 82 2
6
'''


def my_min(name):
    name = name.split()
    name = [int(item) for item in name]
    name.sort()
    tmp = 0
    # for i in range(0, len(name)-1):
    #     if int(name[i+1])-int(name[i]) >= 2:
    #         tmp = int(name[i])+1
    #         break
    for i in range(1, len(name) + 2):
        if i not in name:
            print(i)
            return i
    # if tmp != 0:
    #     return tmp
    # if name[0] > 1:
    #     tmp = 1
    # elif name[0] == 1:
    #     tmp = name[len(name)-1] + 1
    # print(tmp)


while True:
    inp = input("Input: ")
    if len(inp) == 0:
        break
    else:
        my_min(inp)
print("Exit")
