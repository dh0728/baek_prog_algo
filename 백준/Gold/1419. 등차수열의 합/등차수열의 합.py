import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

l = int(input().strip())
r = int(input().strip())
k = int(input().strip())

def counting(low, high ,n):
    if low > high:
        return 0
    return max(0, high // n - (low - 1) // n)

def solution():
    res = 0
    if k == 2:          # 2x + d
        low = max(l, 3) # 첫항 공차 모두 1일 경우 나오는 최소수와 l을 비교우 더 작은 값이 나올수 있는 최소의 합
        res = max(0, r - low + 1) 
    elif k == 3:        # 3(x + d)
        low = max(l, 6)
        res = counting(low, r, 3)
    elif k == 4:        # 2(2x + 3d)
        low = max(l, 10)
        res = counting(low, r, 2)
        if low <= 12 and 12 <= r:
            res -= 1
 
    else:               # 5(x + 2d)
        low = max(l, 15)
        res = counting(low, r,5)

    print(res)     
    return

if __name__ == "__main__":
    solution()