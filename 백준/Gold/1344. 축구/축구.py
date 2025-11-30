import sys
from itertools import combinations
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a = int(input().strip()) / 100.0
b = int(input().strip()) / 100.0

c = [i for i in range(1, 19)]

check = [2, 3, 5, 7, 11, 13, 17] #소수

sa = 0 # A팀 골이 소수일 확률
sb = 0 # B팀 골이 소수일 확률

def solution():
    global sa, sb

    # 확률 구하는 공식
    # p(x) = 18Cx * p**x * (1 - p)**18-x
    for i in range(len(check)):
        comb = len(list(combinations(c, check[i]))) # 18Cx
        sa += comb * pow(a, check[i]) * pow(1.0 - a , 18 -check[i])
        sb += comb * pow(b, check[i]) * pow(1.0 - b , 18 -check[i])

    print(sa + sb - sa*sb) # 적어도 한 팀만 소수면 되니까 각팀이 소수로 골을 넣을 확률을 더한거에서 곱한거를 빼야함


if __name__ == "__main__":
    solution()
