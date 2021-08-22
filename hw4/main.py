'''
Встроенная функция input позволяет ожидать и возвращать данные из стандартного
ввода ввиде строк (весь введенный пользователем текст до нажатия им enter).
Используя данную функцию, напишите программу, которая:
1. После запуска предлагает пользователю ввести целые неотрицательные числа,
разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
2. Получив вводные данные, выделяет полученные числа, суммирует их,
и печатает полученную сумму.
Например:
-> 12 12 12
36
-> 123dfgdr%0&45ty-45--900
-777
'''


def my_sum(name):
    min_ = 0
    tmp = ''
    sum_ = 0
    for i in range(0, len(name)):
        if name[i] == '-' and ord(str(name[i+1])) in range(48, 58):
            min_ = 1
        elif ord(str(name[i])) in range(48, 58):
            tmp = tmp + name[i]
        elif tmp != '':
            if min_ == 1:
                sum_ -= int(tmp)
            else:
                sum_ += int(tmp)
            min_ = 0
            tmp = ''
    if tmp != '':
        if min_ == 1:
            sum_ -= int(tmp)
        else:
            sum_ += int(tmp)
    print(sum_)


while True:
    inp = input("Input: ")
    if len(inp) == 0:
        break
    else:
        my_sum(inp)
print("Exit")

