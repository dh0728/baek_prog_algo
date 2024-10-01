import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())
x_idx=list(map(int,input().split()))

x_set=set(x_idx)   # set으로 중복된 숫자 제거하기
x_list=list(x_set) # 리스트로 변경
x_list.sort()      # 오름 차순 정렬

x_dict={}
for i, x in enumerate(x_list):
    x_dict[x]=i # 인덱스 = 앞에 있는 수의 개수

for i in range(N):
    n=x_dict[x_idx[i]] # n은 현재 좌표의 앞에 있는 수의 개수
    x_idx[i]=n # 좌표 압축 결과로 교체 해주기

print(*x_idx)