'''
Решить несколько задач из projecteuler.net

Решения должны быть максимально лаконичными, и использовать list comprehensions.

problem9 - list comprehension : one line
problem6 - list comprehension : one line
problem48 - list comprehension : one line
problem40 - list comprehension
'''


#problem9
print("problem9")
[[[print(a*b*c) for c in range(b+1, 1000) if a+b+c == 1000 and a**2+b**2 == c**2] for b in range(a+1, 1000)] for a in range(0, 1000)]

#problem6
print("problem6")
print((sum([c for c in range(1, 101)]))**2 - sum([c**2 for c in range(1, 101)]))

#problem48
print("problem48")
print(str(sum([c**c for c in range(1, 1000)]))[::-1][0:10][::-1])

#problem40
print("problem40")
summ = 1
st = ([''.join([str(i) for i in range(1, 10**7)])[10**i-1] for i in range(0, 7)])
for i in st:
    summ *= int(i)
print(summ)


