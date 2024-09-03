import math

T=int(input())
for tc in range(1,T+1):
    x1,y1,r1,x2,y2,r2=map(int,input().split())

    x1_to_x2=math.sqrt((x1-x2)**2+(y1-y2)**2)
    r_sum=r1+r2

    if x1_to_x2==0: # 규현 승환 같은 좌표 일 경우
        if r1==r2:  # 완전 일치시 무한대
            print(-1)
        else:       # 아니면 0
            print(0)
    elif r_sum > x1_to_x2 and abs(r1-r2)< x1_to_x2:  # 규현 승환 사이의 거리보다 r1+r2가 클경우
        print(2)
    elif r_sum == x1_to_x2 or abs(r1-r2)==x1_to_x2: # 규현 승환 사이의 거리와 r1+r2가 같을 경우
        print(1)
    else:  # 작을 경우
        print(0)