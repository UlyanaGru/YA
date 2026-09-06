def CTNumber(num):
    num = ''.join(c for c in num if c.isdigit())
    if len(num) == 11:
        return num[1:]
    else:
        return "495" + num

if __name__ == '__main__':
    must = input().strip()
    for _ in range(3):
        have = input().strip()
        if CTNumber(have) == CTNumber(must): print("YES")
        else: print("NO")
