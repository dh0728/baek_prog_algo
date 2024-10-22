import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def find_seqence(cnt,seq):
    if cnt >= M:
        print(*seq)
        return
    for i in range(N):
        if visited[i]==0:
            visited[i]=1
            find_seqence(cnt+1,seq+[arr[i]])
            visited[i]=0

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

visited=[0]*N
find_seqence(0,[]) #cnt,
