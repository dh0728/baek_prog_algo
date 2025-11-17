import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, score, P = map(int,input().split())


def solution():

    if N == 0:
        print(1)
        return
    
    ranking = list(map(int, input().split()))
    
    if N == P and ranking[-1] >= score: # 랭킹 만석에 태수 점수가 꼴찌보다 작거나 같으면 랭킹 못올라가유
        print(-1)
        return

    rank = 1

    for r in ranking:
        if r > score:
            rank +=1
        else:
            break
    
    print(rank)
    return

if __name__ == "__main__":
    solution()


