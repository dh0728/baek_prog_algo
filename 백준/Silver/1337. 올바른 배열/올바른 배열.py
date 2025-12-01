import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())


arr = []

for _ in range(N):
    n = int(input())
    arr.append(n)

arr.sort()

def solution():
    res = 5
    for i in range(N):
        cnt = 0
        for j in range(arr[i], arr[i] + 5):
            if j not in arr:
                cnt += 1
        if cnt < res:
            res = cnt

    print(res)
    return


if __name__ == "__main__":
    solution()


