from collections import deque

# dfs로 탐색한 결과와 BFS로 탐색한 결과 출력
# 방문할 수 있는 노드가 여러개일 경우 노드 번호가 작은 것을 먼저 방문

# 노드 개수, 에지 개수, 시작 노드 번호
n, m, start = map(int, input().split())

#인접 리스트
list = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    list[s].append(e)
    list[e].append(s)

# 번호가 작은 노드부터 방문하기 위해 정렬
for i in range(n+1):
    list[i].sort()

# 깊이우선 탐색
def dfs(v):
    visitList[v] = True
    print(v, end=' ')
    for i in list[v]:
        if not visitList[i]:
            dfs(i)

visitList = [False]*(n+1)
dfs(start)

# 너비우선 탐색
def bfs(v):
    # queue 자료구조에 시작노드 삽입
    queue = deque()
    queue.append(v)
    # 방문 리스트에 현재 노드 방문 기록
    visitList[v] = True

    # 큐가 비어있을때 까지
    while queue:
        # 큐에서 노드 데이터 가져오기
        now = queue.popleft()
        # 가져온 노드 출력
        print(now, end=' ')

        # 현재 노드의 연결 노드 중 미방문 노드 큐에 삽입하고 방문기록
        for i in list[now]:
            if not visitList[i]:
                queue.append(i)
                visitList[i] = True

print()
visitList = [False]*(n+1)
bfs(start)