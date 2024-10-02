import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

x, y, w, h= map(int,input().split())

min_v=1001

if x >= w/2: # 절반보다 크면
    n1= w-x
else:
    n1= x

if y >= h/2: # 절반보다 크면
    n2= h-y
else:
    n2= y

print(min(n1,n2))