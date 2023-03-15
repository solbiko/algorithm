from heapq import heappush, heappop
import sys

"""
n(1~1,000), m(0~2000,000), k(1~100)
n 도시 수
m 도로 수
k

a b (1~n) c (1~1,000)

1번 시작도시

"""

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력
n, m, k = map(int, input().split())


# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n+1)]

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
# print(graph)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = array = [[INF] * k for _ in range(n+1)]

# 우선순위 큐
q = [(0, 1)] # 가중치 우선이기 때문에 가중치, 목표노드 순서로 저장
distance[1][0] = 0

while q:
    # 우선순위 큐에서 데이터 가져오기 (거리, 노드)
    dist, now = heappop(q)
    # 현재 노드와 연결된 에지 탐색
    for node, cost in graph[now]:
        nCost = dist + cost
        # 새로운 총 거리 = 현재 노드의 거리 + 에지 가중치
        if distance[node][k-1] > nCost:
            # 새로운 노드의 k번째 최단 거리를 새로운 총 거리로 변경하고 거리 순으로 정렬
            distance[node][k-1] = nCost
            distance[node].sort()
            # 우선순위 큐에 새로운 데이터 추가(거리, 노드)
            heappush(q, (nCost, node))

    # print(q)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i][k-1] == INF:
        print(-1)
    else:
        print(distance[i][k-1])