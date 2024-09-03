ch=[0]*31
for _ in range(28):
    n=int(input())
    ch[n]=1

for c in range(1,31):
    if not ch[c]:
        print(c)