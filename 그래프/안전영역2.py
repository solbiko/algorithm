import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline

# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dr=[0,1,0,-1]
dc=[1,0,-1,0]

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
# print(graph)

def DFS(i,j,h):
    visited[i][j]=True

    for d in range(4):
        nextX= i+dr[d]
        nextY= j+dc[d]
        if 0<=nextX<n and 0<=nextY<n and not visited[nextX][nextY] and graph[nextX][nextY] > h:
            visited[nextX][nextY] = True
            DFS(nextX,nextY,h)

res=0
# 구분 작업 수행
for h in range(100):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j]>h:
                cnt+=1
                DFS(i,j,h)
    res=max(res,cnt)

print(res)
