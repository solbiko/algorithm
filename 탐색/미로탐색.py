"""
7*7 격자판 미로를 탈출하는 경로의 가지수를 출력
출발점은 격자의 (1, 1) 좌표이고, 탈 출 도착점은 (7, 7)좌표
격자판의 1은 벽이고, 0은 도로

0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0

위의 지도에서 출발점에서 도착점까지 갈 수 있는 방법의 수는 8가지
"""
import sys
input = sys.stdin.readline

# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dr=[0,1,0,-1]
dc=[1,0,-1,0]

graph= [list(map(int, input().split())) for _ in range(7)]

cnt=0

def dfs(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            nextX=x+dr[i]
            nextY=y+dc[i]
            if 0<=nextX<=6 and 0<=nextY<=6 and graph[nextX][nextY]==0:
                graph[nextX][nextY]=1
                dfs(nextX,nextY)
                graph[nextX][nextY]=0 # 통로로 바꿔줘야 다른길로 back해서 탐색할 수 있음

graph[0][0]=1
dfs(0,0)
print(cnt)