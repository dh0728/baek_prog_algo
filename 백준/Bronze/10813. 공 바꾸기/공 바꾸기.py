def ch_ball(m): # 공바꾸는 함수
    backet[m[0]],backet[m[1]]=backet[m[1]],backet[m[0]]
    return

N,M= map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(M)]

backet=[0]
for i in range(1,N+1): # 바구니에 공 넣기
    backet.append(i)

for a in arr: #교환 방법 순서대로 공 교체
    ch_ball(a)
backet.pop(0)

print(' '.join(map(str,backet)))