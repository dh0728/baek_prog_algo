import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def find_seqence(cnt,seq):
    if cnt >= M:
        result_set.add(tuple(seq)) # set에 삽입해서 중복 제거
        return
    for i in range(N):
        if visited[i]==0:
            visited[i]=1
            find_seqence(cnt+1,seq+[arr[i]])
            visited[i]=0

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

result_set= set()
visited=[0]*N
find_seqence(0,[])
result_list=list(result_set)
result_list.sort() # 순서 맞춰주기
for li in result_list:
    print(*li)
