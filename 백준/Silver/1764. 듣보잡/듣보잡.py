import sys

# N: 듣도 못한 사삼 수, M: 보도 못한 사람
N,M=map(int,sys.stdin.readline().split())

non_lis=[sys.stdin.readline().strip() for _ in range(N)]
non_lis=set(non_lis) # set에 합집합 메서드 사용을 위해 set으로 변환
non_see=[sys.stdin.readline().strip() for _ in range(M)]
non_see=set(non_see) 

intersection_set=non_lis.intersection(non_see) 
result=list(intersection_set) # 사전순 정렬을 위해 리스트로 변환
result.sort()

n=len(result)
print(n)
for i in range(n):
    print(result[i])