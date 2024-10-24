import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def find_seqence(cnt,seq,idx):
    if cnt >= M:
        result_set.add(tuple(seq)) # set에 삽입해서 중복 제거
        return
    for i in range(idx,N):
            find_seqence(cnt+1,seq+[arr[i]],i)

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

result_set= set()
find_seqence(0,[],0)
result_list=list(result_set)
result_list.sort() # 순서 맞춰주기
for li in result_list:
    print(*li)
