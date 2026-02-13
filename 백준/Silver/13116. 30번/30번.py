import sys

n = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    # 문제에서 두 노드가 공통으로 포함되는 꼭지점에 대응된 자연수를 구하라는 것은 부모 노드를 구하는 것이다.
    # 반복문을 통해 두 노드의 가장 가까운 부모 노드를 찾는다.
    while True:

        # 두 노드의 부모 노드가 같으면 반복을 멈춘다.
        if a == b:
            print(a * 10) # 부모 노드의 10배를 출력
            break

        # a가 더 클 경우 a의 부모 노드를 찾는다.
        if a > b:
            a //= 2

        # b가 더 클 경우 b의 부모 노드를 찾는다.
        else:
            b //= 2