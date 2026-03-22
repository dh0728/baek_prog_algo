L, P = map(int, input().split())
p = L*P
for n in map(int, input().split()):
    print(n-p, end=' ')