import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("-inf")

N = int(input().strip())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort()

def find_length(start, end):
    total = 0
    for a, b in arr[1:]:
        # 겹치는 부분이 없는 경우 = 새 선분 등장
        if a > end:
            total += end - start
            start = a

        # 겹치는 부분 있을 경우 - 선분 늘리기
        if b > end:
            end = b
        
        # 포함인 경우는 할짓 없음
    
    total += end - start

    return total

print(find_length(arr[0][0], arr[0][1]))