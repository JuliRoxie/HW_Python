'''
Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
n_arr([2,2])
>> [[“”,“”],[“”,“”]]
n_arr([2,2,2])
>> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]
'''


def array(lst):
    if len(lst) == 1:
        return ['' for i in range(0, lst[0])]
    sp = [array(lst[1:]) for i in range(0, lst[0])]
    return sp


print(array([2, 2]))
print(array([2, 2, 2]))
print(array([2, 3, 2]))
print(array([4, 3, 2]))
print(array([2, 3, 5]))

ar = array([2, 2, 2])
ar[1][1][1] = 'x'
print(ar)
