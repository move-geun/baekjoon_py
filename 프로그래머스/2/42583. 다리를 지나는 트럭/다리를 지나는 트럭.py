from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    bridge_weight = 0
    time = 0
    
    while trucks or bridge_weight > 0:
        bridge_weight -= bridge.popleft()
        time += 1
        
        if trucks and trucks[0]+ bridge_weight <= weight:
            tmp = trucks.popleft()
            bridge.append(tmp)
            bridge_weight += tmp
        else:
            bridge.append(0)
            
    return time