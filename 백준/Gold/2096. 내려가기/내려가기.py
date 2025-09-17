import sys
from itertools import combinations
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

def solution():

    n1, n2, n3 = map(int, input().split())

    # 첫 줄로 초기화
    max_score = [n1, n2, n3]
    min_score = [n1, n2, n3]

    for _ in range(N - 1):

        n1, n2, n3 = map(int , input().split())

        max1 = max(max_score[0], max_score[1]) + n1
        max2 = max(max_score) + n2
        max3 = max(max_score[1], max_score[2]) + n3

        max_score = [max1 , max2, max3]

        min1 = min(min_score[0], min_score[1]) + n1
        min2 = min(min_score) + n2
        min3 = min(min_score[1], min_score[2]) + n3

        min_score = [min1, min2, min3]

    print(max(max_score), min(min_score))



if __name__ == "__main__":
    solution()