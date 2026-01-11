import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input().strip())

def solution():

    for _ in range(T):
        N, M = map(int, input().split())

        cnt = 0
        while N:
            N //= 2
            cnt += 1

        # 황소의 체력을 1까지 깎은 다음 남아있는 먹이를 매일 1개씩 주면 가장 오래삼
        # 2 -> 1 -> 2 -> -> 2 이런식으로 계속 남기 때문에 (반복 횟수 + 먹이 갯수)가 답
        print(cnt + M) 

if __name__ == "__main__":
    solution()

