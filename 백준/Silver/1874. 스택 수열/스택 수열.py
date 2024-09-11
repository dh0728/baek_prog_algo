def cnt_operator():
    stack = []
    max_n = 0
    for _ in range(N):
        n = int(input())
        if not stack:  # 비어있으면 그냥 push
            for i in range(max_n + 1, n + 1):
                stack.append(i)
                result.append('+')
            stack.pop()
            result.append('-')
            if max_n < n:
                max_n = n
        else:
            if n < max_n:
                if stack.pop() != n:
                    return 0
                result.append('-')
            else:
                for i in range(max_n + 1, n + 1):
                    stack.append(i)
                    result.append('+')
                # num=stack.pop()
                if stack.pop() != n:
                    return 0
                result.append('-')
                max_n = n
    return 1

N=int(input())
result=[]
res=cnt_operator()
if res:
    for r in result:
        print(r)
else:
    print('NO')