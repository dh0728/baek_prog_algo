from collections import deque

def solution(bridge_length, weight, truck_weights):

    second = 0
    bridge = deque([0] * bridge_length)
    i = 0
    
    current_weight = 0
    
    while i != len(truck_weights):
        second +=1
        
        current_weight -= bridge.pop()
        
        if(current_weight + truck_weights[i] <= weight):
            current_weight += truck_weights[i]
            bridge.appendleft(truck_weights[i])
            i +=1
        else :
            bridge.appendleft(0)
            
    return second + bridge_length