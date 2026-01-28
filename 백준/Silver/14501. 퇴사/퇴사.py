import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

def bottom_up():
    dp = [0] * (N+1)    # Bottom-up 방식
    for i in range(N):
        for j in range(i+T[i], N+1):
            if dp[j] < dp[i] + P[i]:
                dp[j] = dp[i] + P[i]
    
    print(dp[-1])
    return    

def top_down():
    dp = [0] * (N+1) 
    for i in range(N-1, -1, -1):
        if i + T[i] > N: # 퇴사일이 넘어가는 상담은 X
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], P[i] + dp[i + T[i]]) # i일에 상담을 안할경우 vs i일에 상담을 할경우

    print(dp[0])
    return

def solution():

    top_down()
    return
    
if __name__ == "__main__":
    solution()

