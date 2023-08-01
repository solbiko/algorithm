from collections import deque

def solution(n, edge):
    
    a=[[]*(n+1) for _ in range(n+1)] # 인접리스트
    for s,e in edge:
        a[s].append(e)
        a[e].append(s)

    
    d=[0]*(n+1) # 거리리스트
    visited=[False]*(n+1)
    
    def bfs(v):
        queue = deque()
        queue.append(v)
        
        visited[v]=True
        
        while queue:
            now = queue.popleft()
            for x in a[now]:
                if not visited[x]:
                    visited[x]=True
                    queue.append(x)
                    d[x]=d[now]+1

    bfs(1)
    return d.count(max(d))
