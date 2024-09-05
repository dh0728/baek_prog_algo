N=int(input())

result=0
for n in range(N-1,0,-1):
    str_n=str(n)
    div_n=0
    for s in str_n:
        div_n+=int(s)
    if div_n+n==N:
        result=n

print(result)
