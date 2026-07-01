import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    a,b,c = map(int, input().split())
    abc = sorted([a,b,c])
    print(abc[1])
    pass


if __name__ == '__main__':
    main()
