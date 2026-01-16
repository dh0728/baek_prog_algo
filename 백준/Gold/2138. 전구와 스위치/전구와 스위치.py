import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

off = list(map(bool,map(int, input().strip())))
result = list(map(bool,map(int, input().strip())))

def press_button(bulbs, cnt):
    for i in range(1, N -1):
        if bulbs[i-1] != result[i-1]: # 원하는 상태와 다르면 변경해주기
            cnt +=1
            for j in range(i-1, i+2):   
                bulbs[j] = not bulbs[j]

    # 마지막 전구는 따로처리하기
    if bulbs[N-1] != result[N-1]:
        cnt +=1
        bulbs[N-2] = not bulbs[N-2]
        bulbs[N-1] = not bulbs[N-1]

    if bulbs == result:
        return cnt
    else:
        return -1


def solution():
    
    # 처음부터 결과가 같으면 누를필요 x
    if off == result:
        print(0)
        return
    
    # 0번째 스위치를 누른 상태를 저장하는 리스트
    # - 처음 누르는 스위치를 누르냐 마냐에 따라 나머지는 고정이 되기 때문에 
    on = off.copy()
    on[0] = not on[0]
    on[1] = not on[1]


    off_cnt = press_button(off, 0)

    if off_cnt != -1:
        print(off_cnt)
        return
    else:
        on_cnt = press_button(on, 1)
        if on_cnt != -1:
            print(on_cnt)
            return
    
    print(-1)
    return
    
if __name__ == "__main__":
    solution()

