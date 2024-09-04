sum_n=1
for a in range(3):
    sum_n*=int(input())
ch=[0]*10
for n in str(sum_n):
    ch[int(n)]+=1
for i in range(10):
    print(ch[i])