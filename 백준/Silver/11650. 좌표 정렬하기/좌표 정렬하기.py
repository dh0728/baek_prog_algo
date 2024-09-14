def sort(low,high):
    if high-low <2:
        return
    mid=(low+high)//2 # 중앙값 index
    sort(low,mid)
    sort(mid,high)
    merge(low,mid,high)

def merge(low, mid, high):
    temp=[]
    l,h=low,mid
    while l<mid and h<high:
        if arr[l][0] < arr[h][0]: # 왼쪽 x이 오른쪽 x 보단 작다면
            temp.append(arr[l])
            l+=1
        elif arr[l][0]==arr[h][0]: # 왼쪽 x == 오른쪽 x
            if arr[l][1] < arr[h][1]: # y값 비교해서 더 작은값 넣기
                temp.append(arr[l])
                l+=1

            else:   # 오른쪽 x 가 더 작다면
                temp.append(arr[h])
                h+=1
        else:
            temp.append(arr[h])
            h+=1

    while l<mid:
        temp.append(arr[l])
        l+=1

    while h<high:
        temp.append(arr[h])
        h+=1

    # print(temp)
    for i in range(low,high):
        arr[i]=temp[i-low]

def merge_sort():
    return sort(0,len(arr))

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

merge_sort()
for a in arr:
    print(*a)