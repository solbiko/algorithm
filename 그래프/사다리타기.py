"""
다리 표현은 2차원 평면은 0으 로 채워지고, 사다리는 1로 표현합니다
현수는 특정도착지점으로 도착하기 위해서는 몇 번째 열에서 출발해야 하는지 알고싶습니다. 특정 도착지점은 2로 표기됩니다
특정목적지인 2에 도착하려면 7번 열 출발지에서 출발하면 됩니다.

10*10의 사다리 지도가 주어집니다.

1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1

출발지 열 번호를 출력
"""
import sys
input=sys.stdin.readline

graph=[list(map(int, input().split())) for _ in range(10)]
visited=[[False]*10 for _ in range(10)]

def dfs(r,c): # 행,열
    visited[r][c] = True
    if r==0:
        print(c)
    else:
        # 왼쪽
        if 0<=c-1 and graph[r][c-1]==1 and not visited[r][c-1]:
            dfs(r,c-1)
        # 오른쪽
        elif c+1<10 and graph[r][c+1]==1 and not visited[r][c+1]:
            dfs(r, c+1)
        else: # 위쪽
            dfs(r-1,c)


for i in range(10):
    if graph[9][i]==2: # 밑에서 부터 찾음
        dfs(9,i)

