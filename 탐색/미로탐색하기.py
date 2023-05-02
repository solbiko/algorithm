"""
두 정수 N, M(2 ≤ N, M ≤ 100)
M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dr=[0,1,0,-1]
dc=[1,0,-1,0]

visited= [[False for j in range(m)] for i in range(n)]
d = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    arr = list(input())
    for j in range(m):
        d[i][j]=int(arr[j])
# print(d)

def bfs(i,j):
    queue=deque()
    queue.append((i,j)) 

    visited[i][j]=True
    while queue:
        r,c=queue.popleft()

        for k in range(4): # 상하좌우 탐색
            x= r+dr[k]
            y= c+dc[k]
            while x >=0 and x<n and y>=0 and y<m: # 좌표 유효성 검사
                if d[x][y] !=0 and not visited[x][y]:
                    visited[x][y]=True
                    d[x][y]=d[r][c]+1 # d 리스트에 depth를 현재 노드의 depth +1로 업데이트
                    queue.append((x,y))
                else:
                    break

bfs(0,0)
print(d[n-1][m-1])