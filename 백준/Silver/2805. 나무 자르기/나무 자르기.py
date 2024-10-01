import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def tree_cut():
    s, e = 1, max(tree)  # 범위 1에서 가장 긴 나무 길이
    while s <=e: # 시작과 끝이 역전되면 종료
        mid = (s+e)//2
        total=0
        for t in tree:
            if mid < t:        # 현재 지정한 높이보다 길이가 긴 나무이면
                total += t-mid # 벌목하기

        if total > M:    # 벌목한 나무길이가 벌목하려는 나무보다 크면
            s = mid +1   # 범위 높이기
        elif total < M:  # 벌목한 나무길이가 벌목하려는 나무보다 작으면
            e = mid - 1  # 범위 낮추기
        else:            # 같으면 멈추기
            return mid
    return e


# N 나무의 수, M 집에 가져가려는 나무의 길이
N, M =map(int,input().split())

tree = list(map(int,input().split()))

print(tree_cut())