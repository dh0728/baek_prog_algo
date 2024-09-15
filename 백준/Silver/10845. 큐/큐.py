from collections import deque
N=int(input())

q=deque()
for _ in range(N):
    c=input()
    if c =='front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif c=='back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif c=='size':
        print(len(q))
    elif c=='empty':
        if q:
            print(0)
        else:
            print(1)
    elif c=='pop':
        if q:
           print(q.popleft())
        else:
            print(-1)
    else:
        c_li=list(c.split())
        q.append(c_li[-1])
