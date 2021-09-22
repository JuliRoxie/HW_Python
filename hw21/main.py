'''
Написать функцию-генератор, которая объединяет два отсортированных итератора.
Результирующий итератор должен содержать последовательность в которой содержаться все элементы из каждой коллекции, в упорядоченном виде.

list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]
'''


def merge(a, b):
    lst = []
    while True:
        try:
            itr = next(a)
        except StopIteration:
            break
        else:
            lst.append(itr)
    while True:
        try:
            itr = next(b)
        except StopIteration:
            break
        else:
            lst.append(itr)
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j+1] = tmp
    return iter(lst)


print(list(merge((x for x in range(1, 4)), (x for x in range(2, 5)))) == [1, 2, 2, 3, 3, 4])


