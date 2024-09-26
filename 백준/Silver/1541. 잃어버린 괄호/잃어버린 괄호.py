import sys
input=sys.stdin.readline
#sys.stdin=open('input.txt')

arr=input().strip().split('-') # 마이너스를 기준으로 자르기

num=[] # '-'를 기준으로 나눈 수들을 더한 값이 들어가는 리스트
for a in arr:
    sum_num=0
    sum_n_list=a.split('+') # '+'을 기준으로 나누고
    for s in sum_n_list:
        sum_num += int(s) # 다더하기
    num.append(sum_num) # 더한 값 num 리스트에 삽입

result=num[0] # 처음 값에서 다빼면 정답

for i in range(1,len(num)):
    result -=num[i] # 뒤에 값들 다 빼주기
print(result)