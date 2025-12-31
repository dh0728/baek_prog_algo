import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline
input = sys.stdin.buffer.readline

N = int(input().strip())

# 핵심
# 비감소 수열 S, 평균값 수열 M
# 1. s1 하나만 정하면 모든 si는 결정되나
# 2. 각 si <= mi -> s1에 대한 선형 부등식 (si <= si+1, (si + si+1)/2)
# 3. 모든 부등식을 만족하는 s1의 정수 구간 [L,R]
# 4. 답 max(0, R- L + 1) 
def solution():

    x = int(input().strip()) # m1
    y = int(input().strip()) # m2

    #s₁ ≤ s₂ ≤ s₃
    #(s₁ + s₂)/2 = x(m1)
    #(s₂ + s₃)/2 = y(m2)

    #s₁ ≤ s₂
    #s₁ ≤ 2x − s₁
    #2s₁ ≤ 2x
    #s₁ ≤ x  => s1의 상한은 x

    #s₂ ≤ s₃
    #2x − s₁ ≤ 2y − (2x − s₁)
    #2x − s₁ ≤ 2y − 2x + s₁
    #2s₁ ≥ 4x − 2y
    #s₁ ≥ 2x − y => s1의 하한은 2x -y

    # 결과
    # 2x−y ≤ s1 ≤ x

    # 이걸 s2 =2x−s1 에 대입하면 (비감소 수열이라 s1의 상한일때 s2는 하한)
    a = y           # s2의 하한
    b = 2 * y - x   # s2의 상한

    for _ in range(2, N):
        x = y
        y = int(input().strip())

        #다음 평균값 y = m_i
        # si+1 =2y−si
        # f(t)=2y−t
        # 구간[a,b]를 적용하면
        #최솟값은 f(b) = 2y - b
        #최댓값은 f(a) = 2y - a

        a = 2 * y - a        # 임시 새 상한
        b = max(2*y - b , y) # 임시 새 하한
        a, b = b, a # 뒤집어야 함 기울기가 -1인 선형 함수이기 떄문에 (작은 입력 -> 큰 출력) = 입력 구간 [a, b]출력, 구간은 [f(b), f(a)]

    res = b - a + 1
    if res < 0:
        res = 0

    print(res) 
    
if __name__ == "__main__":
    solution()

