import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N , B = map(int,input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))


# 행렬 곱셈 함수
def matrix_mul(arr1, arr2):

    res = [[0] * N for _ in range(N)] # 연산 결과 
    # 행렬 곱셈 연산 수행
    for row in range(N):
        for col in range(N):
            n = sum(arr1[row][i] * arr2[i][col] for i in range(N))
            res[row][col] = n % 1000
    return res

def div_conquer(n, arr):

    # 종료 조건
    if n == 1:
        return arr
    # n이 짝수
    elif n % 2 == 0:
        half = div_conquer(n//2, arr)
        return matrix_mul(half, half)
    # n이 홀수
    else:
        return matrix_mul(arr, div_conquer(n-1, arr))
        
def solution():
    
    res = div_conquer(B, A)
    for row in res:
        print(*[r%1000 for r in row])
    return


if __name__ == "__main__":
    solution()


