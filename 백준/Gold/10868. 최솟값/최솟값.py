import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

def makeSegmentTree(idx, start, end):

    if start == end: # 리프 노드 일 경우
       segment_tree[idx] = arr[start]
       return segment_tree[idx]

    mid = (start + end) //2

    left = makeSegmentTree(idx * 2, start, mid)
    right = makeSegmentTree(idx * 2 + 1, mid +1, end)
    
    segment_tree[idx] = min(left, right)
    return segment_tree[idx]


def find(idx, start, end, range1, range2):

    # 범위를 완전 벗어날 경우
    if start > range2 or end < range1:
        return 10**9 + 1

    if start >= range1 and end <= range2: # 리프 노드 일 경우
       return segment_tree[idx]

    mid = (start + end) //2

    left = find(idx * 2, start, mid, range1, range2)
    right = find(idx * 2 + 1, mid +1, end, range1, range2)
    
    return min(left, right)
  
arr = [0] + [int(input().strip()) for _ in range(N)]
h = math.ceil(math.log2(N)) + 1
segment_tree = [0] * (1 << h)
makeSegmentTree(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    print(find(1, 1, N, a, b))
