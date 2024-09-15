N=int(input())

stack=[]
for _ in range(N):
    c=input()
    if c =='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif c=='size':
        print(len(stack))
    elif c=='empty':
        if stack:
            print(0)
        else:
            print(1)
    elif c=='pop':
        if stack:
           print(stack.pop())
        else:
            print(-1)
    else:
        c_li=list(c.split())
        stack.append(c_li[-1])