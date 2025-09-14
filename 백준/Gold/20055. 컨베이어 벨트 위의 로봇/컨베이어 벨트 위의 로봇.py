import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N, K = map(int, input().split())

belt1 = deque()
belt2 = deque()
cnt = 0

for i, k in enumerate(list(map(int,input().split()))):

    if i < N:
        belt1.append([k,0]) # 내구도, 로봇번호
    else:
        belt2.append([k,0])


def belt_moving():

    k, r = belt1.pop()

    belt2.appendleft([k, 0]) 
    
    k2, r2 = belt2.pop()

    belt1.appendleft([k2, 0])

    # 벨트가 이동하면서 나가는 칸에 로봇이 있으면 내보내기
    if belt1[N-1][1]:
        belt1[N-1][1] = 0


def robot_moving():

    global cnt

    for i in range(N-2, -1, -1):
        
        if belt1[i][1] and belt1[i+1][1] == 0 and belt1[i+1][0] > 0: # 현재 칸에 로봇이 있고, 다음칸에 로봇이 없으며, 내구도가 1이상이면
            belt1[i+1][1], belt1[i][1] = belt1[i][1] , 0 # 로봇 이동
            belt1[i+1][0] -= 1 # 내구도 감소

            if belt1[i+1][0] == 0: #만약 내구도가 0칸이 생기면
                cnt += 1

            if i+1 == N-1 and belt1[N-1][1]:
                belt1[N-1][1] = 0

    # 로봇 올리기
    if belt1[0][0] > 0 and belt1[0][1] == 0:
        belt1[0][0] -= 1 # 출발칸 내구도 감소
        belt1[0][1] = 1  # 로봇 올리기 
        if belt1[0][0] == 0:
            cnt += 1
        

def solution():
    result = 0
    while cnt < K:
        
        belt_moving()
        robot_moving()
        result += 1
    
    print(result)


if __name__ == "__main__":
    solution()


