import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))

# 출력
print(sum(box) - sum(book))