T=int(input())
for tc in range(1,T+1):
    H, W, N= map(int,input().split()) # H 호텔의 층수 # W 각 층의 방의 수 # N 손님 번호
    floor=N%H
    st=N//H+1
    if not floor:
        floor=H
        st-=1
    print(f'{floor}{st:0>2}')  # 데이터폭=2, 공백시 왼쪽에 0으로 채우기