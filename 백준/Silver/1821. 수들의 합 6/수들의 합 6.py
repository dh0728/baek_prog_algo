import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX_SIZE = 10001

N, F = map(int, input().split()) # N : 가장 윗줄에 있는 숫자 개수 F: 가장 밑에 있는 수

C = [[0] * N for _ in range(N)]
for i in range(N):
    C[i][0] = 1
    C[i][i] = 1
    for j in range(1,i):
        C[i][j] = C[i-1][j-1] + C[i-1][j]

# a    b        c     d
#  a+b     b+c    c+d
#    a+2b+c   b+2c+d
#       a+3b+3c+d

# F = a*C(3,0) + b*C(3,1) + c*C(3,2) + d*C(3,3)
#   = a*1 + b*3 + c*3 + d*1

found = False          # 답 찾았는지 여부(사전순 이므로)
coeff = C[N-1]         # i 번째 위치에 곱해질 계수
used = [False] * (N+1) # 숫자 사용 여부
ans = [0]* N           # 맨 윗줄 숫자들

def dfs(idx, total):
    global found
    if found:
        return
    if idx == N:
        if total == F:
            print(*ans)
            found = True
        return   

    for n in range(1, N+1):
        if not used[n]:
            nxt = total + n * coeff[idx]
            if nxt > F:
                continue

            used[n] = True
            ans[idx] = n
            #print(f"ans ={ans}")
            #print(f"dfs(idx = {idx +1}, nxt={nxt})")
            dfs(idx+1, nxt)
            used[n] = False

def solution():
    
    dfs(0,0)
    return
    
if __name__ == "__main__":
    solution()

