import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def exam_square(x,y,size):
    color=arr[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[i][j] != color: # 다른 색의 종이가 있다면
                return 2
    return color

def make_color_paper(x,y,size):
    global blue_cnt, white_cnt
    sq_color=exam_square(x,y,size)
    if sq_color == 2: # 2이면 다른 색이 섞인 정사각형이므로 잘라야함
        make_color_paper(x, y, size//2) # 다시 4등분으로 쪼개서 검사
        make_color_paper(x+size//2, y, size//2) # (0,0,8)의 예로들면 - > (0,0)(4,0)(0,4)(4,4) 로 쪼개서 다시 검사
        make_color_paper(x,y+size//2, size//2)
        make_color_paper(x+size//2, y+size//2, size//2)
    else:
        if sq_color: # 파란색으로만 이루어진 정사각형을 만들었다면
            blue_cnt+=1
        else: # 하얀색으로만 이루어진 정사각형을 만들었다면
            white_cnt+=1

# N = 2 , 4, 8, 16, 32, 64, 128
N= int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

blue_cnt=0
white_cnt=0

make_color_paper(0,0,N)
print(white_cnt)
print(blue_cnt)
