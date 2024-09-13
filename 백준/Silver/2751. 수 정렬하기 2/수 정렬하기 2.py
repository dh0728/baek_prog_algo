def sort(low,high):
    if high - low <2: #더이상 반으로 쪼갤수 없다면 return
        return
    mid=(low+high)//2 # 중간 값을 찾기
    sort(low,mid) # 왼쪽 재귀로 다시 자르기
    sort(mid,high) # 오른쪽 재귀로 다시 자르기
    merge_arr=merge(low,mid,high) # 자를수 있을 때까지 잘리고 차례로 병합

def merge(low, mid, high):
    temp=[] # 두개의 절반으로 자른 배열ㄹ을 병합한 결과를 저장
    l,h = low,mid # l은 왼쪽 절반 시작점, h은 오른쪽 절반 시작점

    while l<mid and h<high:
        if arr[l] < arr[h]: # 왼쪽 배열 시작 값 < 오른쪽 배열 값
            temp.append(arr[l]) # 왼쪽값 삽입
            l+=1
        else: # 왼쪽 배열 시작 값 > 오른쪽 배열 값
            temp.append(arr[h])
            h+=1

    while l < mid: # 왼쪽에 아직 수가 남아있으면 temp에 차례로 추가(오른쪽값은 모두 사용)
        temp.append(arr[l])
        l +=1

    while h<high: # 오른쪽에 남아있으면(왼쪽값 모두 사용)
        temp.append(arr[h])
        h+=1

    for i in range(low,high): # 병합한 구간만 교체
        arr[i]=temp[i-low] # temp의 크기는 병합한 개수이고 arr크기 수의 총 개수이므로 i-low

def merge_sort():
    return sort(0,len(arr))


N=int(input())
arr=[0]*N
for i in range(N):
    arr[i]=int(input())

merge_sort()
for n in arr:
    print(n)
