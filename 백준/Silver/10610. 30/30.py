import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = input().strip()


def solution():

    # 30의 배수는 3의 배수이면서 10의 배수임 
    if "0" not in N: # 10의 배수 인지 확인
        print(-1)
        return
    
    num = 0
    for n in N:
        num += int(n)
    
    if num % 3 != 0: # 3의 배수인지 확인
        print(-1)
        return

    sorted_num = sorted(N, reverse=True)
    print("".join(sorted_num))


if __name__ == "__main__":
    solution()

