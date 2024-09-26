import sys
input=sys.stdin.readline
#sys.stdin=open('input.txt')

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort(key=lambda x:(x[1], x[0])) # 종료시간을 기준으로 오름차순 정렬하기

cnt = 1
curr_end=arr[0][1]
for i in range(1,N):
    if curr_end <= arr[i][0]: # 현재 회의의 종료 시간과 다음 회의의 시작시간이 크거나 같다면
        cnt+=1 # 이용 가능
        curr_end=arr[i][1] # 현재회의 종료시간 바꾸기
print(cnt)