import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

from collections import deque
def bfs(a):
    global result
    q= deque()
    q.append([a,1])

    while q:
        num , cnt = q.popleft()
        if num == B: # 숫자 찾으면 종료
            result = cnt
            return
        for i in range(2):
            if i ==0:
                new_num =num*2
                if new_num <=B: # 증가시킨 숫자가 찾아야하는 숫자보다 작을 때만 넣기
                    q.append([new_num,cnt+1])
            else:
                new_num = int(str(num)+'1')
                if new_num <= B: # 증가시킨 숫자가 찾아야하는 숫자보다 작을 때만 넣기
                    q.append([new_num,cnt+1])



A ,B =map(int,input().split())
result=-1
bfs(A)
print(result)








