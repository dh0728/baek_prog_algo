import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 책의 개수, M: 박수에 넣을 수 있는 최대 무게

def solution():

    if N  == 0:
        print(0)
        return

    books = list(map(int, input().split()))

    res = 0
    w = 0

    for book in books:
        w += book

        if w > M:
            res += 1
            w = book

    if w > 0:
        res +=1

    print(res)
    return

if __name__ == "__main__":
    solution()

