import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a, b = map(int, input().split())

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True
    
res = []

# 11은 짝수길이를 가지면서 소수인 팰린드롬
if a <= 11 <= b:
    res.append(11)


seed = 1
while True:
    s = str(seed)
    pal = int(s + s[-2::-1])

    if pal > b:
        break
    if pal >= a and isPrime(pal):
        res.append(pal)
    seed += 1

res.sort()

for n in res:
    print(n)
print(-1)
