def cnt_chess_B(x,y):
    cnt=0
    for i in range(x,x+8):
        # i-x %2 ==0 이면 w_chess로 검사
        if (i-x)%2 ==0:
            for j in range(8):
                if arr[i][y+j] != b_chess[j]:
                    cnt+=1
        # i-x %2 ==1 이면 b_chess로 검사
        else:
            for j in range(8):
                if arr[i][y+j] != w_chess[j]:
                    cnt+=1
    result_list.append(cnt)
def cnt_chess_W(x,y):
    cnt=0
    for i in range(x,x+8):
        # i-x %2 ==0 이면 w_chess로 검사
        if (i-x)%2 ==0:
            for j in range(8):
                if arr[i][y+j] != w_chess[j]:
                    cnt+=1
        # i-x %2 ==1 이면 b_chess로 검사
        else:
            for j in range(8):
                if arr[i][y+j] != b_chess[j]:
                    cnt+=1
    result_list.append(cnt)

N,M=map(int,input().split())
w_chess=['W','B','W','B','W','B','W','B']
b_chess=['B','W','B','W','B','W','B','W']
arr=[list(input()) for _ in range(N)]

result_list=[]
for i in range(0,N-7):
    for j in range(0,M-7):
        cnt_chess_W(i,j)
        cnt_chess_B(i,j)

print(min(result_list))