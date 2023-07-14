import math
def solution(n, stations, w):
    answer = 0
    dist=[]

    dist.append(stations[0]-w-1) # 앞
    for i in range(1,len(stations)): # 중간
        dist.append((stations[i]-w-1)-(stations[i-1]+w))
    dist.append(n-(stations[-1]+w)) # 뒤
    
    for i in dist:
        answer += math.ceil(i/(2*w+1))
    
    return answer