import sys
from collections import deque
input = sys.stdin.readline

# 컴퓨터개수, 신례관계개수
n,m,=map(int, input().split())

# 인접 리스트
graph=[[] for _ in range(n+1)]

# 정답리스트
answer=[0]*(n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v]=True

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i]=True
                answer[i]+=1
                queue.append(i)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)


# 모든노드에서 BFS수행
for i in range(1, n+1):
    visited=[False]*(n+1)
    bfs(i)

#print(answer)

m = max(answer)
for i, v in enumerate(answer):
    if v == m:
        print(i, end=' ')