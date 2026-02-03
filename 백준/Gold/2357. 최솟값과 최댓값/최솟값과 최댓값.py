import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split()) 

def makeSegmentTree(idx, start, end):
    if start == end: # 리프노드는 값이 하나라 최대 최소가 등일함
        segment_tree[idx] = (arr[start], arr[start])
        return segment_tree[idx]   # ← 이게 핵심
    
    mid = (start + end) // 2

    left = makeSegmentTree(idx * 2 +1, start, mid) 
    right = makeSegmentTree(idx * 2 + 2, mid + 1, end)

    segment_tree[idx] = (min(left[0], right[0]), max(left[1], right[1]))

    return segment_tree[idx]

def find(idx, start, end, range1, range2):

    # 찾으려는 범위를 벗어나면
    if range1 > end or range2 < start:
        return (10**9 +1, 0)
    
    # 찾으려는 범위에 있으면
    if range1 <= start and end <= range2:
        return segment_tree[idx]
    
    mid = (start + end) // 2
    left = find(idx * 2 +1, start, mid, range1, range2)
    right = find(idx * 2 +2, mid+1, end, range1, range2)
    return (min(left[0], right[0]), max(left[1], right[1]))


h = math.ceil(math.log2(N)) + 1
arr = [int(input().strip()) for _ in range(N)]
segment_tree = [0] * (1 << h)
makeSegmentTree(0, 0, N-1)

def solution():

    for _ in range(M):
        range1, range2 = map(int, input().split())
        res = find(0, 0, N-1, range1-1, range2-1)
        print(res[0], res[1])



    
if __name__ == "__main__":
    solution()