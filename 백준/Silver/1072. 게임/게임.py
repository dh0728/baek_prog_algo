import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

X, Y = map(int, input().split())

def solution():

    Z = (100 * Y) // X
    left = 0
    right = X
    result = X

    if Z >= 99:
        print(-1)
        return

    while left <= right:
        mid = (left + right) // 2
        new_z = (100 * (Y + mid)) // (X + mid)

        if new_z > Z: # 승률이 커지면
            result = mid 
            right = mid - 1 # 왼쪽으로 탐색
        else:
            left = mid + 1 # 오른쪽으로 탐색
    print(result)

if __name__ == "__main__":
    solution()


