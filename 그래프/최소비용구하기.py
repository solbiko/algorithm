import sys
from queue import PriorityQueue

# 도시개수
n=int(input())
#버스개수
m=int(input())
# 최단거리 리스트
d=[sys.maxsize] * (n+1)
# 방문 배열
visited=[False] * (n+1)

# 인접 리스트
graph=[[] for _ in range(n+1)]
for i in range(m):
    # 출발도시, 도착도시, 버스비용
    u,v,w=map(int, input().split())
    graph[u].append((v,w))

start,end=map(int, input().split())


# 다익스트라
def dijkstra(s,e):
    q=PriorityQueue()

    # 출발 노드는 우선순위 큐에 넣고 시작
    q.put((0,s)) # s를 시작점으로 설정
    # 우선순위에 데이터를 최단거리 노드순으로 삽입
    # 거리 리스트에 출발 노드의 값을 0으로 설정
    d[s]=0

    while q.qsize() > 0:

        # 우선순위 큐에서 노드 가져오기
        nowNode = q.get()
        # print(nowNode)
        now=nowNode[1]

        # 현재 선택 노드 방문 여부 확인
        if visited[now]:
            continue
        # 현재 노드 방문 처리
        visited[now] = True

        for i in graph[now]:
            next = i[0]
            value = i[1]
            # 타깃노드 방문전, 타깃노드 최단거리 > 현재선택노드 최단거리+비용
            if not visited[next] and d[next]> d[now]+value:
                # 타깃노드 최단거리 업데이트
                d[next]=d[now]+value
                # 우선순위 큐에 타깃노드 추가
                q.put((d[next], next))

    # 종료 인덱스 최종거리 리턴
    return d[e]

print(dijkstra(start,end))



