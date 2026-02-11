import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, L = map(int,input().split())

arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort()

def cover_counting():
    pos = 0 # 현재까지 판자로 덮인 곳 길이
    total = 0
    for start, end in arr:
        if pos < start: # 아예 안덮인 웅덩이이면
            pos = start
        
        if pos < end: # 아직 다 안덮었으면
            need = end - pos # 덮어야 하는 부분 길이
            cnt = math.ceil(need/L)
            total += cnt
            pos += cnt * L
    return total


print(cover_counting())