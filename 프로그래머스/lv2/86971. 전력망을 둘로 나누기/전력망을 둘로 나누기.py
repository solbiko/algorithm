import copy, sys
def solution(n, wires):
    answer = sys.maxsize
    
    g=[[] for _ in range(n+1)]
    for s,e in wires:
        g[s].append(e)
        g[e].append(s)
    
    visited=[False]*(n+1)

    def BFS(v, tree):
        queue=[]
        visited[v]=True
        queue.append(v)

        while queue:
            now=queue.pop(0)
            visited[now]=True
            for i in tree[now]:
                if not visited[i]:
                    queue.append(i)

    for s,e in wires:
        visited=[False]*(n+1)
        temp=copy.deepcopy(g)
        temp[s].remove(e)
        temp[e].remove(s)
        BFS(s, temp)
        answer = min(answer,abs(n-2*visited[1:].count(True)))
            
    return answer