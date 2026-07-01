import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    path = [['']*m for _ in range(n)]
    dp[0][0] = a[0][0]
    for j in range(1,m):
        dp[0][j] = dp[0][j-1] + a[0][j]
        path[0][j] = 'R'
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + a[i][0]
        path[i][0] = 'D'
    for j in range(1,m):
        for i in range(1,n):
            dp[i][j] = a[i][j] + min(dp[i][j-1],dp[i-1][j])
            if dp[i][j-1]>dp[i-1][j]:
                path[i][j] = 'R'
            else:
                path[i][j] = 'D'
            
    word = []
    i, j = n-1, m-1
    while i>0 or j>0:
        word.append(path[i][j])
        if path[i][j] == 'D': i-=1
        else: j-=1
    word.reverse()
    print(dp[n-1][m-1])
    pass

if __name__ == '__main__':
    main()
    
