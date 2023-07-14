from heapq import heappush, heappop

def solution(operations):
    answer = []
    
    q=[]
    for x in operations:
        o,x = x.split()
        if o=='I':
            heappush(q,int(x))
        elif o=='D':
            if len(q)>0:
                if x=='-1':
                    heappop(q)
                else:
                    q.remove(max(q))    
    if len(q)>1:
        return [max(q), min(q)]
    else:
        return [0,0]
