import sys
# sys.stdin=open('input.txt')

def cnt_lan(l,r):
    while l<=r: # 제일 작은 값과 큰값이 같아지면 종료
        cnt=0
        mid = (l + r) // 2 # 중간값 구하기
        for lan in arr:
            cnt += lan//mid # 중값값으로 잘랐을 때 생성 가능한 랜선 수
        if cnt >= M: # 목표 개수 이상이면 오른쪽(길이 늘려서 다시 계산)
           l  = mid +1
        else:   # 목표개수 보다 작으면 왼쪽(길이 줄여서 다시 계산)
            r = mid-1
    return r


N,M=list(map(int,sys.stdin.readline().split()))
arr=[int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
print(cnt_lan(1,arr[-1]))