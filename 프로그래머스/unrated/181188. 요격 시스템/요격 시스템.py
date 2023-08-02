def solution(targets):
    answer = 1
    
    targets.sort()
    
    start=targets[0][0]
    end=targets[0][1]

    for i in range(1,len(targets)):
        nowStart,nowEnd=targets[i]        
        if end>nowStart:
            end = min(end, nowEnd)
        else: 
            answer+=1
            start,end=nowStart,nowEnd

    return answer