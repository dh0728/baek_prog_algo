import sys
input=sys.stdin.readline


def comb(idx,sum_ki,men_list,cnt):
    global seven_short

    if sum_ki>100: #키의 합이 100을 넘어가면 중지
        return
    if cnt==7: # 7명 다뽑으면
        if sum_ki==100: # 키의 합이 100이면
            seven_short = men_list[:]
            return
        return
    if idx==9: # 마지막 난쟁이까지 다 선택했을 때 조건 만족못하면 중지 
        return

    comb(idx+1,sum_ki+short_men[idx+1],men_list+[short_men[idx+1]],cnt+1) # 현재 난쟁이 선택 O
    comb(idx+1,sum_ki ,men_list,cnt) # 현재 난쟁이를 선택 X

short_men=[0]+[int(input()) for _ in range(9)]
seven_short=[]
visited=[0]*10

comb(0,0,[],0) # 선택 난쟁이수 , 키의 합, 난쟁이들 키 리스트, 선택한 난쟁이 수
seven_short.sort()
for man in seven_short:
    print(man)