# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def my_list(name):
    list_ = []
    tmp = name.split()
    for i in tmp:
        if i not in list_:
            list_.append(i)
    print(' '.join(list_))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Input')
    inp = input()
    my_list(inp)

