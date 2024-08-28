N=int(input())  # N 수열 길이

arr=list(map(int,input().split())) 

state=1     # state=1 이면 점점 커지는 경우, 0이면 작아지는 경우
cnt=1       # 수열길이 세는 변수
sm=0        # 같은 수 반복을 세는 변수
max_cnt=0   #가장 긴 수열
for i in range(N-1):
    if arr[i] < arr[i+1]: # 점점 커지는 경우
        if state:   # 점점 커지고 있는경우
            cnt+=1
        else: 
            state=1 # 점점 작아지다가 다시 커지는 경우
            if max_cnt < cnt: # 초기화 전 max_cnt와 길이 비교
                max_cnt =cnt
            cnt = sm + 2
        sm=0
    elif arr[i]> arr[i+1]: # 점점 작아지는 경우
        if state == 0:
            cnt+=1
        else:
            state=0 # 점점 커지다가 다시 작아지는 경우
            if max_cnt < cnt: # 초기화 전 max_cnt와 길이 비교
                max_cnt =cnt
            cnt = sm + 2
        sm=0
    else: # 같은 경우
        cnt+=1  # 길이 +1
        sm +=1  # 중복 횟수 +1
if max_cnt < cnt:   # 수열순회 끝난후 cnt 와 길이 비교
    max_cnt=cnt
    
print(max_cnt)