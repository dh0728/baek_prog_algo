import sys
import heapq
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

m, n = map(int, input().split())

dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
        '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

l = []

for i in range(m, n+1):
    a = ' '.join([dict[j] for j in str(i)])
    l.append([i, a])
    
l.sort(key=lambda x:x[1])

for i in range(len(l)):
    if i%10 == 0 and i!= 0:
        print()
    print(l[i][0], end=' ')