arr=list(map(int,input().split()))

if arr[0]==1:
    state=1
else:
    state=0
for i in range(len(arr)-1):
    if state==1 and arr[i]+1 == arr[i+1]:
        continue
    elif state==0 and arr[i]-1 == arr[i+1]:
        continue
    else:
        state=-1
        break

if state==1:
    print('ascending')
elif state==0:
    print('descending')
else:
    print('mixed')