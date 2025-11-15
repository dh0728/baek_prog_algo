import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]    
words.sort(key = len) 

# 접두사가 되는 단어는 항상 다른 단어보다 길이가 작거나 같음
# 문자열이 짧은 순서대로 정렬하고 자기꺼보다 뒤에 있는 단어와만 비교 ㄱㄱ
def solution():

    res = 0
    for i in range(N):
        is_prefix = False

        # 길이가 더 긴 단어만 검사
        for j in range(i + 1, N):
            if j >= N:
                break
            
            if words[i] == words[j][0:len(words[i])]:
                is_prefix = True
                break

        if not is_prefix:
            res +=1

    print(res)
    return

if __name__ == "__main__":
    solution()


