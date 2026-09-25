import sys


def ALoopInGraph():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    data = sys.stdin.read().split()
    answ = []
    n = int(len(data)**(1/2))
    for i in range(n):
        j = i*n + i
        if data[j] == '1':
            answ.append(str(i))
    if answ:
        print('\n'.join(answ))
    else:
        print('NO LOOPS')
    pass


if __name__ == '__main__':
    ALoopInGraph()