import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def cnt_S(center,end):
    cnt=0
    if center =='O':
        between='I'
    else:
        between='O'
    for i in range(N,end): # N 번째 idx부터 검사시작
        if S[i]==center: # P 문자열의 중앙값이면 검사 시작
            for j in range(1,N+1): # 범위 index 넘어가지 않는 범위선에서 검사
                if j%2:  # j=홀수이면 i+j에 문자는 중앙값 옆에 문자와 문자 같음 
                    if S[i+j] != between or S[i-j] !=between:
                        break
                else:   # j=짝수이면 i+j열의 문자는 center와 같음
                    if S[i+j] != center or S[i-j] !=center:
                        break
            else: #break 된적이 없으면 찾은 것
                cnt+=1
    return cnt

N=int(input())
S_len=int(input())
S=input().strip()

result=0
if N%2: #홀수
    result=cnt_S('O',S_len-N) # P이 홀수이면 P문자열의 중앙은 O
else:
    result=cnt_S('I',S_len-N) # 짝수이면 I

print(result)