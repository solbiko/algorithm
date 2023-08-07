import sys
input=sys.stdin.readline
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m,k=map(int, input().split())
a=[input() for _ in range(n)]
x1,y1,x2,y2=map(int, input().split())

dist = [[-1]*m for _ in range(n)]
dist[x1-1][y1-1] = 0
q = deque([(x1-1,y1-1)])

while q:
    x,y = q.popleft()
    for d in range(4):
        for nk in range(1,k+1):
            nx=x+nk*dx[d]
            ny=y+nk*dy[d]
            if not (0<=nx<n and 0<=ny<m) or a[nx][ny] == '#':  break
            if -1 != dist[nx][ny] <= dist[x][y]:  break
            if -1 != dist[nx][ny]:  continue
            dist[nx][ny]=dist[x][y]+1
            q.append((nx,ny))

# for i in range(n):
#     for j in range(m):
#         print(dist[i][j], end="  ")
#     print()

print(dist[x2-1][y2-1])