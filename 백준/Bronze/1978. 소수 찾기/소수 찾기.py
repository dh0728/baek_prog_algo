N=int(input())
arr= list(map(int,input().split()))
cnt=0 # 소수 개수

for a in arr:
    if a==1:
        continue
    state=1
    for i in range(2,a):
        if a%i==0:
            state=0
            break
    if state:
        cnt+=1
print(cnt)