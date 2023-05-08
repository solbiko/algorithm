"""
현수의 농장은 N*N 격자판, 각 격자안에는 한 그루의 사과나무가 심어저 있다, N의 크기는 항상 홀수
사과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.

입력
첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
각 격자안의 사과의 개수는 100을 넘지 않는다.

출력
수확하는 사과의 총 개수

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

"""
from collections import deque

# 네 방향 탐색을 위한 상수
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
visited= [[False]*n for _ in range(n)] # BFS 시 방문 여부 저장 리스트

sum=0 # 수확하는 사과의 총 개수

queue = deque()
visited[n//2][n//2]=True
sum+=graph[n//2][n//2]
queue.append((n//2,n//2))

L=0
while True:
    if L==n//2:
        break
    for _ in range(len(queue)): # 큐사이즈만큼
        tmp=queue.popleft()
        for d in range(4): # 네방향
            nextX=tmp[0]+dx[d]
            nextY=tmp[1]+dy[d]
            if not visited[nextX][nextY]:
                sum+=graph[nextX][nextY]
                visited[nextX][nextY]=True
                queue.append((nextX, nextY))
    L+=1
print(sum)