"""
시간초과
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

p, q = map(int, input().split())

houses=list(map(int,input().split()))
stores=list(map(int,input().split()))

distance = [INF] * (n+1)
min_dist, answer = INF, 0

for store in stores:
    heap = []
    heappush(heap, (0, store))
    min_dists=[INF]*(n+1)
    min_dists[store] = 0


    while heap:  # 큐가 비어있지 않다면
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heappop(heap)
        if now in houses:  # 최단 경로를 갱신했기 때문에 더 이상 수행하지 않음
            break
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if min_dists[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if min_dists[i[0]] > cost and i[0] != store:  # 집 노드들의 최단 경로 갱신
                min_dists[i[0]] = cost
                heappush(heap, (cost, i[0]))
            distance[i[0]] = min(distance[i[0]], min_dists[i[0]])  # 전체 최단 경로 갱신

for house in houses:
    if min_dist > distance[house]:
        min_dist = distance[house]
        answer = house

print(answer)