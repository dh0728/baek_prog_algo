import math

def solution(fees, records):
    cars = {}
    fees_list = []
    answer = []
    
    for i in range(len(records)):
        time, car, in_out = records[i].split() # 문자열 자르기
        if in_out == "IN" :  # 입차이면
            if cars.get(car): # 차가 이미 주차한 기록이 있으면
                cars[car][1] = time # 재입차
            else :
                cars[car] = [0, time] # 현재까지 주차시간, 입차시간
            
        else : # 출차이면
            in_hour, in_min = cars[car][1].split(':')
            out_hour, out_min = time.split(':')
            parking_time = (int(out_hour) * 60 +  int(out_min)) - (int(in_hour) * 60 + int(in_min))
            cars[car] = [parking_time + cars[car][0], '0'] # 주차시간 갱신후 입차시간 초기화
    
    
    
    # 출차하지 않은 자동차 출차시키기
    # 주차비용 계산하기 (정렬)
    
    for car, value in cars.items():
        if value[1] != '0':
            in_hour, in_min = value[1].split(':')
            parking_time = ( (23 * 60 + 59) - ( int(in_hour) * 60 + int(in_min)) )
            cars[car] = [parking_time + cars[car][0], '0'] # 주차시간 갱신후 입차시간 초기화
        
    # 주차비용 계산하기 (총 누적시간으로 계산 후 차량번호 오름차순)
    for car, value in cars.items():
        total_time = value[0]
        fees_list.append([int(car), cal_fee(fees, total_time)])
    
    fees_list.sort()
    
    for i in range(len(fees_list)):
        answer.append(fees_list[i][1])
        
    return answer


def cal_fee(fees, time):
    base_t, base_f, unit_t, unit_f = fees
    if time <= base_t:
        return base_f
    extra = time - base_t
    return base_f + math.ceil(extra / unit_t) * unit_f







