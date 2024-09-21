import sys
input=sys.stdin.readline


# 수열 만드는 함수 
def make_arr(N):  #N:수열의 길이 
    num_arr=[] 
    cnt=0
    curr_num=1
    for i in range(N):
        if cnt==curr_num: # 숫자를 숫자번 넣었으면
            cnt=0 # 넣은 횟수 초기화
            curr_num+=1 # 다음 숫자로 넘어가기
        num_arr.append(curr_num)
        cnt+=1
    return num_arr

def sum_arr(s,e):
    sum=0
    for i in range(s,e):
        sum+=arr[i]
    return sum

start,end =map(int,input().split())
arr=make_arr(end)
result=sum_arr(start-1,end) # index = 0 부터 숫자를 넣어줘서 start -1 
print(result)