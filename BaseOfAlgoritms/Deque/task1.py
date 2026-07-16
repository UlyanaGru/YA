from collections import deque
dq = deque()
all = list()
q = int(input())
for _ in range(q):
    line = input().split()
    a = int(line[0])
    if a == 1:
        b = int(line[1])
        dq.append(b)
        all.append(str(dq[0]))
    elif a == 2:
        if dq:
            dq.popleft()
            if dq: all.append(str(dq[0]))
            else: all.append(str(-1))
        else: all.append(str(-1))
            
print('\n'.join(all))