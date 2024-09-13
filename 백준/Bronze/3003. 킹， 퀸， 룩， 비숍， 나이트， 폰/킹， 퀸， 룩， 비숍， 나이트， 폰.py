arr=list(map(int,input().split()))
piece=[1,1,2,2,2,8]
result=[0]*len(piece)
for i in range(len(arr)):
    if arr[i] !=piece[i]:
        result[i]=piece[i]-arr[i]

print(*result)
