import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K= map(int, input().split())

def solution():

    q = deque()

    for i in range(1, N+1):
        q.append(i)

    res = []
    cnt = 0
    while q:
        cnt +=1
        n = q.popleft()
        
        # K 번째 사람이면
        if cnt == K:
            res.append(n)
            cnt = 0
        else: # K 번쨰 아니면 맨뒤로 보내기
            q.append(n)

    print("<", end="")
    print(", ".join(f"{n}" for n in res), end= "")
    print(">")
    return

if __name__ == "__main__":
    solution()


