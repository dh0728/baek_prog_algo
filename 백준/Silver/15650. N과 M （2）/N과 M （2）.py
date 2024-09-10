def find_sequence(cnt,seq):
    if cnt>=M:
        print(*seq)
        return
    for n in range(1,N+1):
        if n <= seq[-1]: # 전 숫자보다 작으면 pass
            continue
        find_sequence(cnt+1,seq+[n])

# 1부터 N까지 중복없이 M개를 고른 수열
N,M=map(int,input().split())
select=[0]*(N+1)
for n in range(1,N+1): # 수열을 첫 숫자를 넣어 주면서 시작
    find_sequence(1,[n]) # 선택한 숫자 개수, 수열리스트