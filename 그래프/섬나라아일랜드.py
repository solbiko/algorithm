"""
섬은 1로 표시되어 상하좌우와 대각선으로 연결되어 있음. 0은 바다
섬나라 아일랜드에 몇 개의 섬이 있는지

첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다. 두 번째 줄부터 격자판 정보가 주어진다.
7
1 1 0 0 0 1 0
0 1 1 0 1 1 0
0 1 0 0 0 0 0
0 0 0 1 0 1 1
1 1 0 1 1 0 0
1 0 0 0 1 0 0
1 0 1 0 1 0 0
"""
import sys
input=sys.stdin.readline
from collections import deque

# 여덟 방향 탐색을 위한 상수
dr=[0,1,0,-1,-1,1,1,-1]
dc=[1,0,-1,0,1,1,-1,-1]

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
# print(graph)

def BFS(i,j):
    global cnt
    queue=deque()
    graph[i][j]=0
    queue.append([i,j])

    while queue:
        print(queue)
        r,c=queue.popleft()
        for d in range(8): # 네방향+대각선
            nextX= r+dr[d]
            nextY= c+dc[d]
            if 0<=nextX<n and 0<=nextY<n and graph[nextX][nextY]==1:
                graph[nextX][nextY] = 0 # 방문표시, 바다로 만듬
                queue.append([nextX, nextY])
    cnt+=1

cnt=0

# 구분 작업 수행
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            BFS(i,j)

print(cnt)