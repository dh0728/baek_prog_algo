import sys
input=sys.stdin.readline

words = [input().strip() for i in range(5)] # 단어들 삽입

for j in range(15):
    for i in range(5):
        if j < len(words[i]): #현재 단어의 순서가 그 단어의 최대 길이보다 작을 경우만 출력
            print(words[i][j], end='')
print()