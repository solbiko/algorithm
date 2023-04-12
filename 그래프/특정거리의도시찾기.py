from heapq import heappush, heappop
import sys
input = sys.stdin.readline


# 도시, 거리, 거리정보, 출발노드
n,m,k,x = map(int, input().split())

# 최단거리 리스트
d = [sys.maxsize] * (n+1)

# 인접 리스트
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

q = []
heappush(q, (x))
d[x] = 0

while q:
    now=heappop(q)

    for i in graph[now]:
        if d[i]>d[now]+1:
            d[i]=d[now]+1
            heappush(q, i)

cnt=0
for i in range(1, n+1):
    if d[i]==k:
        cnt+=1
        print(i)
if cnt==0:
    print(-1)