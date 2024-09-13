def sort(low,high):
    if high - low <2:
        return
    mid=(low+high)//2
    sort(low,mid)
    sort(mid,high)
    merge_arr=merge(low,mid,high)

def merge(low, mid, high):
    temp=[]
    l,h = low,mid

    while l<mid and h<high:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l+=1
        else:
            temp.append(arr[h])
            h+=1
    while l < mid:
        temp.append(arr[l])
        l +=1
    while h<high:
        temp.append(arr[h])
        h+=1
    for i in range(low,high):
        arr[i]=temp[i-low]

def merge_sort():
    return sort(0,len(arr))


N=int(input())
arr=[0]*N
for i in range(N):
    arr[i]=int(input())

merge_sort()
for n in arr:
    print(n)
