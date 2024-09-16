import sys

N,M=map(int,sys.stdin.readline().split()) # N 도감에 수록되어 있는 포겟몬 수
                                          # M 내가 맞춰야 하는 문제 수 M

monster_dict=[sys.stdin.readline().strip() for _ in range(N)]
for _ in range(M):
    case=sys.stdin.readline().strip()

    if case.isalpha():
        print(monster_dict.index(case)+1)
    else:
        print(monster_dict[int(case)-1])