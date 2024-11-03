import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def sol(n,start,i,j):
    '''
    재귀로 4분면으로 계속 잘라가면서 i,j의 현재 사분면을 구하고
    잘린 사분면을 기준으로 i,j값을 수정해준다.
    n==0 일때는 1개의 사분면에 1개의 좌표가 있으므로 사분면의 시작지점(start)가 결국 구하고자하는 답이다.
    '''

    if n==0: # n==1이면 답 구할 수 있음
        print(start)
        return

    cnt =2 ** (n - 1) # 한 사분면의 변의 길이
    one_idx_cnt= cnt**2    # 한 사분면의 좌표 수

    # 현재 n에서 목표 좌표가 몇 사분면인지 구해야함
    if i < cnt and j >= cnt: # 1 사분면
        start = start+ one_idx_cnt * 1 # 현재 사분면에서의 시작 좌표
        j -= cnt                # 현재 사분면 기준으로 j 값 수정
        sol(n-1, start, i, j)        # 현재 사분면에서 또 4개의 사분면으로 잘라서 재귀호출
    elif i < cnt and j < cnt: # 2 사분면
        start = start + one_idx_cnt * 0
        sol(n - 1, start, i, j)
    elif i >= cnt and j < cnt: # 3사분면
        start = start + one_idx_cnt * 2 # 현재 사분면에서의 시작 좌표
        i -= cnt
        sol(n - 1, start, i, j)
    else: # 4사분면
        start = start + one_idx_cnt * 3 # 현재 사분면에서의 시작 좌표
        i -= cnt
        j -= cnt
        sol(n - 1, start, i, j)
    return
N, r, c = map(int,input().split())

sol(N,0,r,c)
