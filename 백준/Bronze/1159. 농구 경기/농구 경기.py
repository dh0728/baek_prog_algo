import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

from collections import Counter

def find_starters(players):
    first_letters = [player[0] for player in players]  # 각 선수 성의 첫 글자를 추출
    letter_count = Counter(first_letters)  # 첫 글자의 빈도 계산

    # 5명 이상인 첫 글자만 필터링
    starters = [letter for letter, count in letter_count.items() if count >= 5]
    
    if starters:
        # 사전순 정렬 후 출력
        return ''.join(sorted(starters))
    else:
        # 선발할 수 없으면 "PREDAJA" 출력
        return "PREDAJA"

# 입력 받기
N = int(input())  # 선수의 수
players = [input().strip() for _ in range(N)]  # 선수 이름 입력

# 결과 출력
result = find_starters(players)
print(result)