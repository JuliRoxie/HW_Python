'''
https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2. (Please note that the palindromic number,
in either base, may not include leading zeros.)

Напишите программу, которая решает описанную выше задачу и печатает ответ.
'''


sum_ = 0
for i in range(0, 1000001):
    if str(i)[::-1] == str(i) and "{0:b}".format(i)[::-1] == "{0:b}".format(i):
        sum_ += i
print("Sum =", sum_)

