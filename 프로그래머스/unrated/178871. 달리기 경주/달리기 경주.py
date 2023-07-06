def solution(players, callings):
    
    callings
    p={x:i+1 for i,x in enumerate(players)}
    r={i+1:x for i,x in enumerate(players)}

    
    for x in callings:
        pre=r[p[x]-1]
        p[x]-=1
        rank=p[x]
        p[pre]+=1
        r[rank]=x
        r[rank+1]=pre
        
    return list(r.values())