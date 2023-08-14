from collections import namedtuple
from heapq import heappush, heappop
INF=float('inf')

Problem = namedtuple('Problem', ['cost', 'nalp', 'ncop', 'ralp', 'rcop'])

def solution(alp, cop, problems):

    dist={(alp,cop):0}
    visited=set()
    q=[]
    
    problems=[Problem(cost, nalp, ncop, ralp, rcop) for nalp, ncop, ralp, rcop, cost in problems ]
    problems+=[Problem(1,0,0,1,0), Problem(1,0,0,0,1)]
    
    max_alp=max(p.nalp for p in problems)
    max_cop=max(p.ncop for p in problems)
    
    heappush(q, (0,alp,cop))
    
    while q:
        d,a,c = heappop(q)
        
        if (a,c) in visited:
            continue
        else:
            visited.add((a,c))
            
        for p in problems:
            newa, newc = min(a+p.ralp, max_alp), min(c+p.rcop, max_cop)
            newcost=d+p.cost
            if a>=p.nalp and c>=p.ncop and newcost < dist.get((newa, newc), INF):
                dist[(newa, newc)] = newcost
                heappush(q, (newcost, newa, newc))

    return dist[(max_alp, max_cop)]
            