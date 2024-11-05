import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())
file = list(map(int, input().split()))
size = int(input())
total = 0

for i in range(N):
    if file[i] > size:
        if file[i] % size == 0:
            total += file[i] // size
        else:
            total += file[i] // size + 1
    elif file[i] == 0:
        total += 0
    else:
        total += 1

print(size*total)