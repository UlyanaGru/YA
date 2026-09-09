def DEq(a,b,c):
    if a == 0 and b != c**2:
        print('NO SOLUTION')
    elif c < 0:
        print('NO SOLUTION')
    elif a != 0:
        if (c**2 - b) % a == 0:
            print((c**2 - b)//a)
        else:
            print('NO SOLUTION')
    elif a == 0 and b == c**2:
        print('MANY SOLUTIONS')

if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    DEq(a,b,c)