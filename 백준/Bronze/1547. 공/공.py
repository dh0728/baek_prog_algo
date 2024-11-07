import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

m = int(input())
arr = [0,1,2,3]

for i in range(m):
    x,y = map(int,input().split())
    arr[x],arr[y] = arr[y], arr[x]
print(arr.index(1))