import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())


def solution():

    q = deque()

    for _ in range(N):

        command = list(input().split())
        com = command[0]
        if com == "push": #
            q.append(int(command[1])) # 큐에 넣기
        
        elif com == "pop":
            if q:
                print(q.popleft())
            else:
                print(-1)

        elif com == "size":
            print(len(q))

        elif com == "empty":
            if q:
                print(0)
            else:
                print(1)
            
        elif com == "front":
            if q:
                print(q[0])
            else:
                print(-1)
        else: # back
            if q:
                print(q[-1])
            else:
                print(-1)
    return

if __name__ == "__main__":
    solution()


