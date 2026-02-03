import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MOD = 1000000007
N, M, K = map(int, input().split())  # N: 수의 개수 M: 수의 변경이 일어나는 횟수 K: 구간의 곱을 구하는 횟수

def makeSagmentTree(idx, start, end):

    if start == end: # 리프 노드
       segment_tree[idx] = arr[start]
       return segment_tree[idx]
       
    mid = (start + end)//2
    left = makeSagmentTree(idx * 2, start, mid)
    right = makeSagmentTree(idx * 2 + 1, mid + 1, end)

    segment_tree[idx] = (left * right) % MOD
    return segment_tree[idx]

def find(idx, range1, range2, start, end):

    if start > range2 or end < range1: #범위를 벗어나면
        return 1
    
    if start >= range1 and end <= range2:
        return segment_tree[idx]
    
    mid = (start + end)//2

    left = find(idx * 2, range1, range2, start, mid)
    right = find(idx * 2 +1, range1, range2, mid + 1, end)

    return (left * right) % MOD

def update(idx, start, end, target, value):
    
    # 변경한 수가 범위에 포함되지 않는 경우 : 고칠거 없음
    if target < start or target > end:
        return segment_tree[idx]
    
    if start == end:
        segment_tree[idx] = value
        return segment_tree[idx]
    
    # 포함되는 경우
    mid = (start + end)//2
    left =update(idx * 2, start, mid, target, value)
    right = update(idx * 2 + 1, mid+1, end, target, value)

    segment_tree[idx] = (left * right) % MOD
    return segment_tree[idx]


h = math.ceil(math.log2(N)) + 1
segment_tree = [0] * (1 << h)
arr = [0] + [int(input().strip()) for _ in range(N)]
makeSagmentTree(1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1: # 
        arr[b] = c
        update(1, 1, N, b, c)
    else:
        print(int(find(1, b, c, 1, N)) % MOD )