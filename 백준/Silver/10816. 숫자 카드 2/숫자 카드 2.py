import sys
# sys.stdin=open('input.txt')
# input=sys.stdin.readline()

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
num_list=list(map(int,sys.stdin.readline().split()))

cnt_list=[0]*20000001 # 개수를 카운팅하는 배열 생성
for a in arr:
    cnt_list[a]+=1 # 개수만큼 +1

for n in num_list:
    print(cnt_list[n], end=' ')
print()