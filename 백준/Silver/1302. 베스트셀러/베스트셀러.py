import sys
import collections
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

def solution():

    books = {}

    for _ in range(N):
        book = input().strip()

        if book in books:
            books[book] +=1 # 이미 팔린적 있으면
        else:
            books[book] = 1 # 처음 팔린책이면

    books_sort = sorted(books.items())

    result = sorted(books_sort, key = lambda x : x[1], reverse= True)

    print(result[0][0]) 


if __name__ == "__main__":
    solution()


