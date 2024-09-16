import sys
# sys.stdin=open('input.txt')
# input=sys.stdin.readline()

def binary_search(n):
    l=0
    r=N-1
    result=0

    while l<=r: # 왼쪽이 오른쪽 같거나 커지면 종료
        mid = (l+r)//2 # 중간값
        if arr[mid]==n: # 숫자를 찾으면
            result=1
            break  # 반복문 종료
        elif n > arr[mid]: # 중간값이 찾는 숫자보다 크면
            l = mid+1   # 절반으로 쪼갠 배열에서 오른쪽 배열 탐색
        else:           # 작으면
            r= mid-1    # 왼족 배열 탐색
            
    return result

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
find_li=list(map(int,sys.stdin.readline().split()))

arr.sort()
for n in find_li:
    print(binary_search(n))
