from collections import deque

N=int(input())

q=deque()
for i in range(1,N+1):
    q.append(i)

while len(q)>1:
    remove=q.popleft()
    move_bottom=q.popleft()
    q.append(move_bottom)

print(q.popleft())
