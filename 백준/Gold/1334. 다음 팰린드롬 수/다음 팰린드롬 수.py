import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = input().strip()
SIZE = len(N)

def make_pal(front, is_even):
    # 자릿수가 변하지 않으면 현재 front로 팰린드롬수 만들기    
    if is_even: # 홀수
        return front + front[-2::-1]
    else:
        return front + front[::-1]
    


def is_palindrome(n):

    is_even = SIZE % 2 # 홀수면 1, 짝수면 0

    if is_even: # 홀수
        front = N[:SIZE//2+1]
    else: # 짝수
        front = N[:SIZE//2]
    
    # 1) 현재 숫자에서 일안 팰린드롬 만들어보기
    cand = make_pal(front, is_even)

    if cand > N:
        return cand

    next = str(int(front) + 1)

    # 2) 현재 숫자에서 불가능하면 앞에 숫자뽑아서 현재 자릿수에서 가능한지 확인하기
    if len(next) > len(front): # 불가능하면 False 반환
        return False
    # 3) 가능하면 front에서 + 1 해서 만들고 반환
    res = make_pal(next, is_even)

    return res


def solution():
    
    res = is_palindrome(N)
    
    if res:
        print(res)
        return
    
    # 현재 자릿수의 숫자에서 팰린드롬 수가 없을 경우
    size = len(N)
    print(pow(10, size) + 1)
    return


if __name__ == "__main__":
    solution()
