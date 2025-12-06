import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def solution():

    data = input().strip()
    count0 = 0 # 전부 0으로 바뀌는 경우
    count1 = 0 # 전부 1로 바꾸는 경우

    # 첫 번째 원소에 대해서 처리
    if data[0] == '1':
        count0 += 1
    else:
        count1 += 1
       

    # 두 번째 원소부터 모든 원소를 확인한다.
    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            # 다음 수에서 1로 바뀌는 경우
            if data[i + 1] == '1':
                count0 += 1
            else:
                count1 += 1

    print(min(count0, count1))

if __name__ == "__main__":
    solution()
