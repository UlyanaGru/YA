def BTriangular(a,b,c):
    if (a + c > b) and (b + a > c) and (c + b > a):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    print(BTriangular(a,b,c))