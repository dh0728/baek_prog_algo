import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def find_seqence(cnt,seq):
    if cnt >= M:
        result_set.add(tuple(seq))
        return
        # if seq in result:
        #     return
        # result.append(seq)
        # return
    for i in range(N):
        if visited[i]==0:
            visited[i]=1
            find_seqence(cnt+1,seq+[arr[i]])
            visited[i]=0

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

result=[]
result_set= set()
visited=[0]*N
find_seqence(0,[])
# print(result_set)
result_list=list(result_set)
result_list.sort()
for li in result_list:
    print(*li)
