import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())

ans = 0

while bin(n).count('1') > k:
    i = bin(n)[::-1].index('1')
    n += 2 ** i 
    ans += 2 ** i

print(ans)