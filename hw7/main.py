'''
Напишите программу, которая читает данные из файлов
/etc/passwd и /etc/group на вашей системе и выводит
следующую информацию в файл output.txt:
1. Количество пользователей, использующих все имеющиеся
интерпретаторы-оболочки.
( /bin/bash - 8 ; /bin/false - 11 ; ... )
2. Для всех групп в системе - UIDы пользователей
состоящих в этих группах.
( root:1, sudo:1001,1002,1003, ...)
'''


def passwd():
    file = open("/etc/passwd", "r")
    mass1 = []
    mass2 = []
    while True:
        # считываем строку
        line = file.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        else:
            line = line.rstrip('\n')
            line = line.split(':')
            if line[6] in mass1:
                mass2[mass1.index(line[6])] += 1
            else:
                mass1.append(line[6])
                mass2.append(1)
    for i in range(0, len(mass1)):
        print(mass1[i], '-', mass2[i])
    file.close()


def group():
    file = open("/etc/group", "r")
    mass1 = []
    mass2 = []
    while True:
        # считываем строку
        line = file.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        else:
            line = line.rstrip('\n')
            line = line.split(':')
            mass1.append(line[0])
            mass2.append(line[2])
    file.seek(0)
    while True:
        # считываем строку
        line = file.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        else:
            line = line.rstrip('\n')
            line = line.split(':')
            k = str(line[3])
            k = k.split(',')
            for i in range(0, len(k)):
                if k[i] in mass1:
                    k[i] = mass2[mass1.index(k[i])]
            if k != ['']:
                print(line[0] + ":" + mass2[mass1.index(line[0])] + "   UID: " + ", ".join(k))
            else:
                print(line[0] + ":" + mass2[mass1.index(line[0])])

    file.close()


print("Количество пользователей, использующих интерпретаторы-оболочки:")
passwd()
print("UIDы пользователей состоящих в группах:")
group()


