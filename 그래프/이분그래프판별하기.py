import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 테스트케이스
n=int(input())
# 이분그래프 판별함수
isEven=True

def dfs(node):
    global isEven
    # 현재 노드 방문 기록
    visited[node]=True
    for i in graph[node]:
        if not visited[i]:
            # 인접 노드는 같은 집합이 아니므로 다른 집합으로 처리
            check[i]=(check[node]+1)%2
            dfs(i)
        elif check[node]==check[i]:
            # 이미 방문한 노드가 현재 내 노드와 같은 집합이면 이분 그래프 아님
            isEven=False


for _ in range(n):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)] # 그래프 데이터 저장 인접리스트
    visited=[False]*(v+1) # 방문 기록 저장 리스트
    check=[0]*(v+1) # 노드별 집합 저장 리스트
    isEven=True # 이분 그래프 판별 변수 초기화

    # 인접 리스트로 그래프 저장
    for i in range(e):
        start,end=map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(1,v+1):
        if isEven:
            dfs(i)
        else:
            break

    # print(check)
    print("YES" if isEven else "NO")