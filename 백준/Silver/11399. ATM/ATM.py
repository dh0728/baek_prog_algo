import sys
input=sys.stdin.readline


N=int(input())
arr=list(map(int,input().split()))
arr.sort() # 오름차순으로 정렬

total_wait=0 # 합의 최솟값 초기화
wait=0 # 사람당 기다리는 시간 
for a in arr:
    wait+=a # 사람당 기다리는 시간은 전사람들 기다린시간 + 자기자신 뽑는 시간
    total_wait+=wait 

print(total_wait)