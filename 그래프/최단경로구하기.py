import sys
from queue import PriorityQueue
"""
다익스트라
에지의 가중치가 10 이하의 자연수인 방향 그래프
시작점에서 다른 모든 노드의 최단경로

노드의 개수 v(1~20,000), 에지의 개수 e(1~300,000)
출발번호 k
에지 정보 u v w (u에서 v로가는 가중치 w)
두 노드 사이에 에지가 2개이상 존재할 수 있음

시작점은 0, 경로가 없을 경우 INF 출력
"""

# 노드, 엣지의 갯수
v, e = map(int, input().split())
# 시작점
k = int(input())

q = PriorityQueue()

# 최단거리 리스트
distance = [sys.maxsize] * (v+1)

# 방문 배열
visited = [False] * (v+1)

# 인접 리스트
graph = [[] for _ in range(v+1)]

for i in range(e):
    u, v, w = map(int, input().split())  # 가중치가 있는 인접 리스트 저장
    # 인접리스트에 에지 정보 저장
    graph[u].append((v,w))


# 출발 노드는 우선순위 큐에 넣고 시작
q.put((0,k)) # k를 시작점으로 설정
# 거리 리스트에 출발 노드의 값을 0으로 설정
distance[k] = 0



while q.qsize() > 0:

    # 우선순위 큐에서 노드 가져오기
    current = q.get()
    c_v = current[1]

    # 현재 선택 노드 방문 여부 확인
    if visited[c_v]:
        continue
    # 현재 노드 방문 처리
    visited[c_v] = True
    for tmp in graph[c_v]:
        next = tmp[0]
        value = tmp[1]

        # 연결 노드의 최단거리 > 연결 노드 방문전 and 현재 노드 최단 거리 + 비용
        if distance[next] > distance[c_v] + value:
            # 연결 노드 최단 거리 업데이트
            distance[next] = distance[c_v] + value
            # 우선 순위 큐에 연결 노드 추가
            q.put((distance[next], next))

for i in range(1,v+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
        