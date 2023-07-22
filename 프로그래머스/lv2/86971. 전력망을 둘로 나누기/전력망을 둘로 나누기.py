import copy, sys
def solution(n, wires):
    answer = sys.maxsize
    
    g=[[] for _ in range(n+1)]
    for s,e in wires:
        g[s].append(e)
        g[e].append(s)
    
    visited=[False]*(n+1)

    def BFS(v, e):
        del_wire=[[v,e], [e,v]]
        queue=[]
        visited[v]=True
        queue.append(v)

        while queue:
            now=queue.pop(0)
            visited[now]=True
            for i in g[now]:
                if not visited[i] and [now,i] not in del_wire:
                    queue.append(i)

    for s,e in wires:
        visited=[False]*(n+1)
        BFS(s, e)
        answer = min(answer,abs(n-2*visited[1:].count(True)))
            
    return answer