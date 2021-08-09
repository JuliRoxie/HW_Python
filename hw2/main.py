'''
Встроенная функция input позволяет ожидать и возвращать данные из стандартного
ввода в виде строк (весь введенный пользователем текст до нажатия им enter).
Используя данную функцию, напишите программу, которая:

1. После запуска предлагает пользователю ввести текст, содержащий любые слова,
слоги, числа или их комбинации, разделенные пробелом.
2. Считывает строку с текстом, и разбивает его на элементы списка, считая
пробел символом разделителя.
3. Печатает этот же список элементов (через пробел), однако с удаленными
дубликатами.

Пример:
-> asdfdsf324 ?3 efref4r4 23r(*&^*& efref4r4 a a bb ?3
asdfdsf324 ?3 efref4r4 23r(*&^*& a bb
'''


def my_list(name):
    list_ = []
    tmp = name.split()
    for i in tmp:
        if i not in list_:
            list_.append(i)
    print(' '.join(list_))


print('Input:')
inp = input()
my_list(inp)

