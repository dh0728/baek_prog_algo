import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def cal_protector(student):
    if student <= 0: # 남은 응시생이 없으면, 부감독관은 필요없음
        return 0
    if student%C:
        return student//C +1
    else:
        return student//C

N = int(input()) # 시험장 수
A = list(map(int,input().split())) # 응시자수

B, C = map(int,input().split()) # B 총감독관이 감시할 수 있는 응시자수
                                # C 부감독관이 감시할 수 있는 응시자수

cnt=len(A) # 총갑독관수은 기본으로 1명씩 있음
for n in A:
    cnt+=cal_protector(n-B) # 총감독관이 감시하는 응시생 빼고 함수 호출

print(cnt)