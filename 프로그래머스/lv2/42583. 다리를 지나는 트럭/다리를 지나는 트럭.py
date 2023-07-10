from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    w=0 # 다리에 올라간 트럭들 무게
    wq=deque(truck_weights) # 대기트럭 큐
    bq=deque([0 for _ in range(bridge_length)]) # 다리 큐

    time=0
    while len(wq) or w>0:
        w-=bq.popleft()

        if len(wq) and w+wq[0]<=weight:
            n = wq.popleft()
            w+=n
            bq.append(n)
        else:
            bq.append(0)
        
        time+=1   
    return time