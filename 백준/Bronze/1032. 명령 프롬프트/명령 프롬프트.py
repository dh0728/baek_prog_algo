import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def is_same(st):
    w=files[0][st]
    for i in range(1,N):
        if files[i][st] !=w:
            return '?'
    return w

N = int(input())
files= [input().strip() for _ in range(N)]
result=''
file_len=len(files[0])
for j in range(file_len):
    result +=is_same(j)
print(result)