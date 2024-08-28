def count_sum():
    cnt=0
    for i in range(101):
        for j in range(101):
            if map[i][j]:
                cnt+=1
    return cnt

def check_square(sq):
    x1,y1,x2,y2=sq[0],sq[1],sq[2],sq[3]
    for j in range(x1,x2):
        for i in range(y1,y2):
            map[i][j]=1

arr=[list(map(int,input().split())) for _ in range(4)]
map=[[0]*101 for _ in range(101)]
# print(map)
for a in arr:
    check_square(a)

result=count_sum()
print(result)