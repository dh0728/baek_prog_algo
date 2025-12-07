import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline



def solution():

    n = int(input().strip())

    line = 0
    end = 0

    # 1/1
    # 1/2 2/1
    # 3/1 2/2 1/3
    # 1/4 2/3 3/2 4/1
    # 5/1 4/2 3/5 2/4 1/5
    # 짝수줄 갈수록 분자 +1 분모 -1
    # 홀수줄 갈수록 분자 -1 분모 +1 

    while n > end: # 현재줄 -> 다음줄로 갈때마다 분수갯수 1씩 증가
        line += 1
        end += line

    diff = end - n

    if line % 2: #홀수 라인
        top = diff + 1
        bottom = line - diff 
    else:
        top = line - diff
        bottom = diff + 1

    print(f"{top}/{bottom}")

if __name__ == "__main__":
    solution()