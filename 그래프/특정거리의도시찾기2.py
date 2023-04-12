import sys
from collections import deque
input = sys.stdin.readline


# 도시, 거리, 거리정보, 출발노드
n,m,k,x=map(int, input().split())

# 방문 거리 저장 리스트
d=[-1]*(n+1)

# 인접 리스트
graph=[[] for _ in range(n+1)]

# 정답리스트
answer=[]

def bfs(v):
    queue = deque
    queue.append(v)
    d[v]+=1
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if d[i] == -1:
                d[i] = d[now] + 1
                queue.append(i)


for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

bfs(x)

for i in range(n+1):
    if d[i]==k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in range:
        print(i)