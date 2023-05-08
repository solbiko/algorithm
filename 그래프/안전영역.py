"""
어떤 지역의 높이 정보를 파악, 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사
비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠김
안전영역 : 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역

높이가 4 이하인 모든 지점이 물에 잠김
내리는 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5
높이가 6이하인 지점을 모두 잠기게 만드는 많은 비가 내리면 물에잠기지 않는 안전한 영역은 아래 그림에서와 같이 네 개가 됨


과 열의 개수를 나타내는 수 N
둘째 줄부터 N 개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보
높이는 1이상 100 이하의 정수

5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""

import sys
from collections import deque
input=sys.stdin.readline

# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dr=[0,1,0,-1]
dc=[1,0,-1,0]

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
# print(graph)

def BFS(i,j,h):
    global cnt
    queue=deque()
    queue.append([i,j])
    visited[i][j]=True

    while queue:
        r,c=queue.popleft()
        for d in range(4):
            nextX= r+dr[d]
            nextY= c+dc[d]
            if 0<=nextX<n and 0<=nextY<n and not visited[nextX][nextY] and graph[nextX][nextY] > h:
                visited[nextX][nextY] = True
                queue.append([nextX, nextY])

res=0
# 구분 작업 수행
for h in range(100):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j]>h:
                cnt+=1
                BFS(i,j,h)
    res=max(res,cnt)

print(res)
