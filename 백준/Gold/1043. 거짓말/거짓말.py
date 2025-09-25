import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 사람수, 파티수
N ,M = map(int,input().split())

# 진실을 아는 사람 리스트 index = 0 은 사람수 뒤로 번호 나열됨
t_list = list(map(int, input().split()))

party = [list(map(int, input().split())) for _ in range(M)]

def solution():

    if t_list[0] == 0: # 진실을 아는 사람이 없으면 파티 수만큼 리턴
        print(M)
        return 

    result = 0
    black_list = set(t_list[1:])

    changed =True

    while changed:
        changed = False
        for p in party:
            attends = p[1:]

            # 파티에 블랙 한명이라도 있으면 참석자 전부 블랙
            if any(x in black_list for x in attends):
                for x in attends:
                    if x not in black_list:
                        black_list.add(x)
                        changed = True
    
    for p in party:
        attends = p[1:]

        if all(x not in black_list for x in attends):
            result += 1
    
    print(result)
    return
    
            

if __name__ == "__main__":
    solution()


