import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((i, b))
    graph[b].append((i, a))


def dijkstra():
    d = [sys.maxsize for _ in range(n + 1)]
    d[1] = 0

    q = []
    heapq.heappush(q, (0, 1)) # 시작 노드 1

    while q:
        cost, node = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if d[node] < cost:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인

        for ncost, nnode in graph[node]:

            # 주기
            tmp = (cost-ncost)//m
            if (cost - ncost) % m != 0:
                tmp+=1
            ntime = ncost+tmp*m

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if d[nnode] > ntime+1:
                d[nnode] = ntime+1
                heapq.heappush(q, (ntime+1, nnode))
    return d[n]

print(dijkstra())