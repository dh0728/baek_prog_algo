from collections import deque

def solution(bandage, health, attacks):
    
    time = bandage[0]     #시전시간
    heal = bandage[1]     #초당회복량
    heal_add = bandage[2] #추가회복량
    
    queue = deque(attacks)
    
    cnt = 0 # 연속 선공횟수
    
    hp = health
    
    attack = queue.popleft() # 첫번째 공격
    for s in range(attacks[-1][0] + 1):
        
        ## 공격을 받은 경우
        if (attack[0] == s):
            hp -= attack[1]
            if (hp <= 0): # 체력이 다 떨어지면
                return -1 
            
            cnt = 0
            if queue: # 새로운 공격 꺼내야함
                attack = queue.popleft()
        
        ## 공격을 안받은 경우
        else:
            cnt +=1 ##연속 붕대감기 횟수 +1
            if( cnt == time):
                hp += heal_add
                cnt = 0
            
            hp += heal
            if (hp > health): # 최대 체력 이상 X
                hp = health
    
    return hp