import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


L, R = input().split()

def eight_counting(n):
    cnt = 0
    return cnt

def solution():

    res = 0

    L_len = len(L)
    R_len = len(R)

    if L_len == R_len: # 자릿수가 같은 경우
        
        # 숫자가 완전 동일한 경우
        if L == R:
            for c in L:
                if c == "8":
                    res +=1

        # 숫자는 다른 경우
        else:
            for i in range(L_len):
                if L[i] == R[i] and L[i] == "8": # 두 숫자 모두 8이면
                    res +=1
                
                if L[i] != R[i]: # 자릿수 값다르면 다른수가 올수 있음. 카운팅 종료
                    break
                
    else: # 두수 자릿수가 다른 경우
        pass

    print(res)
    return



if __name__ == "__main__":
    solution()


