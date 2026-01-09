import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
res = [-1 for _ in range(N)]
def solution():

    # 뒤에서 앞으로 N -2 -> 0
    for i in range(N-2 , -1, -1):
        if arr[i] != arr[i+1]:
            res[i] = i + 2 # 답은 1부터 시작하니까 1+
        else:
            res[i] = res[i + 1] # 뒤부터 결론을 내기 때문에 같은 수의 경우 앞에껀 뒤와 결과가 같음
    
    for n in res:
        print(n, end=" ")

if __name__ == "__main__":
    solution()
