import sys


def GListToMatrix():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    answ = []
    for i in range(n):
        ncol = input().split()
        row = [0]*n
        if ncol:
            for col in ncol:
                row[int(col)] = 1
            answ.append(' '.join(map(str, row)))
        else:
            answ.append(' '.join(map(str, [0]*n)))
    print('\n'.join(answ))
        


if __name__ == '__main__':
    GListToMatrix()
