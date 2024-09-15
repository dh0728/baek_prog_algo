import sys
# sys.stdin=open('input.txt')
# sys.stdin.readline() 쓰자

from collections import deque


T=int(sys.stdin.readline())
for tc in range(1,T+1):
    N,M=map(int,sys.stdin.readline().split()) # N 문서수, M 인쇄순서가 궁굼한 문서가 현재 놓인 위치
    priority=list(map(int,sys.stdin.readline().split()))
    q=deque()
    p_sort=sorted(priority) #우선순위 검사를 위해 중요도 오름차순으로 한 배열 복사

    for i in range(N):
        q.append([i,priority[i]])
    idx=0
    while q:
        doc_loc, doc_p=q.popleft()
        if doc_p==p_sort[-1]: # 현재 큐에서 우선순위가 가장크다면
            idx+=1
            if doc_loc == M: # 인쇄 순서가 궁금한 문서를 찾으면
                print(idx)
                break
            p_sort.pop() # 우선순위 젤 큰거 하나빼주기
        else:
            q.append([doc_loc,doc_p])
