# 깊이우선탐색
# 단절점 찾기, 단절선 찾기, 사이클 찾기, 위상정렬
# 재귀함수/스택

# 노드 방문 여부 체크할 배열
# 그래프 인접 리스트로 표현 (인접행렬이나 인접 리스트로 표현)
# 후입선출 -> 스택 -> 스택 성질을 갖는 재귀함수로 풀기

# 방향없는 그래프가 주어졌을 때 연결 요소의 갯수 구하기

# 노드, 엣지의 갯수
n, m = map(int, input().split())

#인접 리스트
list = [[] for _ in range(n+1)]

# 방문기록 리스트
visitList = [False]*(n+1)

# 재귀함수
def dfs(v):
    visitList[v] = True
    for i in list[v]:
        if not visitList[i]:
            dfs(i)

for _ in range(m):
    # 방향이 업는 그래프 양쪽 에지 모두 저장
    s, e = map(int, input().split())
    list[s].append(e)
    list[e].append(s)


cnt = 0

for i in range(1, n+1):
    if not visitList[i]:
        cnt += 1 # 연결 노트 중 방문하지 않았던 노드만 탐색
        dfs(i)

print(cnt)

