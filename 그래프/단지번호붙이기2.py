# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dr=[0,1,0,-1]
dc=[1,0,-1,0]

n=int(input())
graph=[list(map(int, input())) for _ in range(n)]
# print(graph)

res= []

def dfs(x,y):
    global cnt
    cnt+=1
    graph[x][y]=0 # 방문처리
    for i in range(4): # 네방향
        nextX=x+dr[i]
        nextY=y+dc[i]
        if 0<=nextX<n and 0<=nextY<n and graph[nextX][nextY]==1:  # 지도 격자
            dfs(nextX,nextY)

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt=0
            dfs(i,j)
            res.append(cnt)

print(len(res))
res.sort()
for i in res:
    print(i)
