import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def find_sequence(cnt,num,seq):
    if cnt >= M:
        print(*seq)
        return
    for n in range(num,N+1):
        find_sequence(cnt+1,n,seq+[n])
    return

N, M =map(int,input().split())
visited=[0]*(N+1)
find_sequence(0,1,[])
