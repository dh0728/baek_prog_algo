import sys
input=sys.stdin.readline

def find_x_y(control):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    x,y=0,0
    angle=0
    x_set=set()
    y_set=set()
    x_set.add(0) # 초기 좌표 넣기
    y_set.add(0)
    for c in control:
        if c=='L':
            angle=(angle-1)%4
        elif c=='R':
            angle=(angle+1)%4
        elif c=='F': # 앞으로 한칸
            x += dxy[angle][0]
            y += dxy[angle][1]
            x_set.add(x)
            y_set.add(y)
        else: # 뒤로 한칸
            x -= dxy[angle][0]
            y -= dxy[angle][1]
            x_set.add(x)
            y_set.add(y)
    return (max(x_set)-min(x_set)) * (max(y_set)-min(y_set))

T=int(input())
for tc in range(1,T+1):
    control_list=input().strip()
    result=find_x_y(control_list)
    print(result)