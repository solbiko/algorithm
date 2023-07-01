def solution(cacheSize, cities):
    answer=0
    q=[]
    
    if cacheSize==0:
        return len(cities)*5
    
    for x in cities:
        x = x.upper()
        if x in q:
            answer+=1
            q.remove(x)
            q.append(x)
        else:
            answer+=5
            if len(q)>cacheSize-1:
                q=q[1:]
            q.append(x)
    return answer