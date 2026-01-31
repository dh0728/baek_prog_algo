import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))


# 두 구간의 누적합 나머지가 같으면, 그 사이 구간의 합은 M으로 나누어 떨어짐 ㄷㄷ
def solution():

    sum_num = 0
    remainder = [0] * M
    for i in range(N):
        sum_num += arr[i]
        remainder[sum_num % M] += 1
        
    res = remainder[0]
    for remain in remainder:
        res += (remain * (remain - 1)) // 2 # rC2  

    print(res)
    return
    
if __name__ == "__main__":
    solution()