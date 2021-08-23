'''
Написать функцию-генератор, которая объединяет два отсортированных итератора.
Результирующий итератор должен содержать последовательность в которой содержаться все элементы из каждой коллекции, в упорядоченном виде.

list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]
'''


def merge(a, b):
    full = []
    for i in a:
        full.append(i)
    for i in b:
        full.append(i)
    full.sort()
    return full


print(list(merge((x for x in range(1, 4)), (x for x in range(2, 5)))) == [1, 2, 2, 3, 3, 4])


