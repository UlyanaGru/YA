import sys


def EMatrixToList():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    data = sys.stdin.read().split()
    answ = []
    n = int(len(data)**(1/2))
    i = 0
    while i <= len(data):
        loc = []
        for j in range(len(data[i:i+n])):
            if data[i:i+n][j] == '1':
                loc.append(str(j))
        answ.append(' '.join(loc))
        i += n
    print('\n'.join(answ))


if __name__ == '__main__':
    EMatrixToList()
