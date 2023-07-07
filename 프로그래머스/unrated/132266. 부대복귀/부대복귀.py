from collections import deque

def solution(n, roads, sources, destination):
    
    q = deque([destination])

    graph = [[] for _ in range(n+1)]
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)

    visit = [-1]*(n+1)
    visit[destination] = 0
    
    while q:
        now = q.popleft()

        for x in graph[now]:
            if visit[x] == -1:
                visit[x] = visit[now]+1
                q.append(x)

    return [visit[i] for i in sources]