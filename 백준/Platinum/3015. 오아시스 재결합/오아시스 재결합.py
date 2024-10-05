import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

def count_pair(N):
    arr = [0] + [int(input()) for _ in range(N)]
    s = [[0, 0]]
    cnt_arr = [0] * (N + 1)

    # 현재 사람 기준 왼쪽에서 볼 수 있는 사람 수를 세자
    for i in range(1, N + 1):
        cnt = 1
        while 0 < s[-1][0] <= arr[i]:  # 현재 사람 기준 왼쪽 사람이 작거나 같으면 계속 빼자
            h_pop, cnt_pop = s.pop()
            cnt_arr[i] += cnt_pop

            # 현재 사람을 s에 넣기 위한 cnt 정의하기
            if h_pop == arr[i]:  # 키가 같으면
                cnt += cnt_pop
            else:  # top의 사람의 키가 현재 사람보다 더 작으면
                cnt = 1

        if s[-1][0] != 0:  # 왼쪽에 사람이 있을 경우 = 볼 수 있는 사람 +1
            cnt_arr[i] += 1

        s.append([arr[i], cnt])

    return sum(cnt_arr)

N = int(input())
print(count_pair(N))