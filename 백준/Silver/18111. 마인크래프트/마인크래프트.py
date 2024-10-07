import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def cal_time(h):
    remove_n = 0
    add_n = 0

    for i in range(257):
        if block[i]==0: # 블록 없으면 패스
            continue
        if i < h: # 높이차가 음수이면 블록을 삽입해야함
            add_n += (h-i)*block[i]
        elif i >h: # 높이차가 양수이면 블록을 제거해야함
            remove_n += (i-h)*block[i]

    if (remove_n + B) >=add_n: # 블록이 충분하면
        t = remove_n*2 + add_n # 시간 구하기
        return t
    else:
        return 99999999999999

N, M, B= map(int,input().strip().split())

block=[0]*257
for i in range(N):
    for a in list(map(int,input().strip().split())):
        block[a]+=1

min_time=99999999999999
height =0

for x in range(257): # 0~256까지 모든 높이로 만드는 시간을 구해서 찾기
    time = cal_time(x)
    if time <= min_time: # 최소 시간일 경우 저장
        min_time = time
        height=x

print(min_time,height)