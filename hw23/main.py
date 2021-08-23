'''
Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
n_arr([2,2])
>> [[“”,“”],[“”,“”]]
n_arr([2,2,2])
>> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]
'''


def array(lst):
    sp = []
    sp = ["" for i in range(0, lst[0])]
    if len(lst) == 1:
        return sp
    for i in range(1, len(lst)):
        tmp = []
        for j in range(0, lst[i]):
            tmp.append(sp)
        sp = tmp
    return sp


print(array([2, 2]))
print(array([2, 2, 2]))
print(array([2, 3, 2]))
print(array([4, 3, 2]))
print(array([2, 3, 5]))
