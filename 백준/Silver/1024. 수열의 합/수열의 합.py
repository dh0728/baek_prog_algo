N, L = map(int, input().split())

result = []
temp = 0

while(1):
    """  N과 L의 몫과 나머지를 활용해 중간값으로 두고 계산하려고 했음 -> 94%에서 틀렸음 -> 모든 반례를 찾아보고 넣어도 맞게 나옴 -> "가장 짧은" 코드가 아니라고 결론
    a = N//L
    b = N%L
    if (b == 0):
        start = a - L//2
        end = a + L//2
    else:
        start = a - b + 1
        end = a + b
    """

    start = int((2*N-L*L+L)*(2*L)**(-1)) #등차수열의 합 공식을 이용해 첫 항 찾기
    end = start + L -1

    if (start < 0): #음수가 나올 경우 0부터 카운트
        start += abs(start)
        end += abs(start)

    for i in range(start, end+1):
        result.append(i)
        temp += i

    if(temp == N):
        break
    else:
        result = []
        temp = 0
        L += 1
        if (L > 100):
            result.append(-1)
            break

for k in result:
    print(k, end=" ")