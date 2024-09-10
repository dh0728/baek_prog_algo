def find_sequence(cnt,seq):
    if cnt>=M:
        print(*seq)
        return
    for n in range(1,N+1):
        if select[n]:
            continue
        if n < seq[-1]:
            continue
        select[n]=1
        find_sequence(cnt+1,seq+[n])
        select[n]=0

# 1부터 N까지 중복없이 M개를 고른 수열
N,M=map(int,input().split())
select=[0]*(N+1)
for n in range(1,N+1):
    select[n] = 1
    find_sequence(1,[n]) # 선택한 숫자 개수, 수열리스트
    select[n] = 0