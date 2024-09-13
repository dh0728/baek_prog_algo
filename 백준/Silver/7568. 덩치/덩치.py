N=int(input())
arr=[]
for i in range(N):
    p=tuple(map(int,input().split()))
    arr.append(p)

for i in range(len(arr)):
    rank=1
    for j in range(len(arr)):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            rank+=1
    print(rank, end=' ')
print()