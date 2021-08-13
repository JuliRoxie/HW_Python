'''
Написать функцию Фиббоначи fib(n), которая вычисляет
элементы последовательности Фиббоначи:
1 1 2 3 5 8 13 21 34 55 .......
'''


def fib(n):
    k = []
    for i in range (0, n):
        if i == 0 or i == 1:
            k.append(1)
        else:
            k.append(k[i-2]+k[i-1])
    print(k)

print("n:")
fib(int(input()))