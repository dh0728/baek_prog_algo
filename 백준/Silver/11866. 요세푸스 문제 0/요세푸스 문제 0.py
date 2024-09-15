from collections import deque
N,M=map(int,input().split())
q=deque()
for i in range(1,N+1):
    q.append(i)

print('<', end='')
cnt=1
while len(q)>1:
    if cnt==M: # 3번째 수마다 빼서 프린트해주기
        n=q.popleft()
        print(f'{n},', end=' ')
        cnt=1
    else: # 3번째 아니면 빼서 뒤로 넣기
        n=q.popleft()
        q.append(n)
        cnt+=1
print(q.popleft(), end='')
print('>')
