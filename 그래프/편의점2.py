"""
집을 고르는 기준을 편의점과의 거리가 가장 가까운 곳으로 하려한다.
영선이가 이사할 도시는 정점과 간선으로 표현할 수 있는데, 이사가려 하는 집의 후보들과 편의점은 정점들 위에 있다.
영선이는 캠프 강사 준비로 바쁘므로, 대신하여 집을 골라주자.

처음 줄에는 정점의 개수 n, 간선의 개수 m이 주어진다.(2 ≤ n ≤ 5,000, 1 ≤ m ≤ 100,000)
다음 m줄에는 a,b,c가 주어지는데 이는 a, b를 잇는 간선의 거리가 c라는 것이다.(1 ≤ a, b ≤ n, 1 ≤ c ≤ 10,000)
다음 줄에는 집의 후보지의 개수 p와 편의점의 개수 q가 주어진다.(2 ≤ p+q ≤ n, 1 ≤ p, 1 ≤ q)
다음 줄에는 집의 후보지들의 정점번호, 그 다음줄에는 편의점의 정점번호가 주어진다. 집의 후보지와 편의점은 서로 겹치지 않는다.
6 9
1 4 1 <- a, b를 잇는 간선의 거리가 c
1 5 2
1 6 3
2 4 2
2 5 3
2 6 1
3 4 3
3 5 1
3 6 2
3 3 <-  집의 후보지의 개수 p와 편의점의 개수 q
1 2 3 <- 집의 후보지들의 정점번호
4 5 6 <- 편의점의 정점번호
"""

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distance = [INF] * (n+1)

# 힙
queue = []

# 다익스트라
def dijkstra():
    while queue:
        dist, now = heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]: # 인접노드마다
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heappush(queue, (cost, i[0]))

p, q = map(int, input().split())
houses=list(map(int,input().split()))
stores=list(map(int,input().split()))
houses.sort()

# 편의점마다 시작점 큐에 삽입
for i in stores:
    heappush(queue, (0, i))

# 다익스트라
dijkstra()

min_dist = INF
mid_node = 0

for i in houses:
    if distance[i] < min_dist:
        min_dist = distance[i]
        min_node = i

print(min_node)