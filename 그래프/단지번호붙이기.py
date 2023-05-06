"""
1은 집이 있는 곳을, 0은 집이 없는 곳
연결된 집들의 모임인 단지를 정의하고, 단지에 번호 붙이려한다
단지수를 출력, 각 단지 에 속하는 집의 수를 오름차순으로 정렬하여 출력

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
import copy
from collections import deque

# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dr=[0,1,0,-1]
dc=[1,0,-1,0]

n=int(input())
graph=[list(map(int, input())) for _ in range(n)]
visited= [[False]*n for _ in range(n)]
# print(graph)

no=1 # 단지 번호
dList=list([]) # 단지 리스트
dangi=[] # 단지

def addNode(i,j,q):
    graph[i][j] = no  # 단지 번호 저장
    visited[i][j] = True  # 방문 표시
    dangi.append([i,j])
    q.append([i,j])

def BFS(i,j):
    queue=deque()
    queue.append([i,j])
    dangi.clear()
    dangi.append([i,j])
    visited[i][j]=True
    graph[i][j]=no

    while queue:
        r,c=queue.popleft()
        for d in range(4): # 네방향
            nextR= r+dr[d]
            nextC= c+dc[d]
            if 0<=nextR<n and 0<=nextC<n: # 지도 격자
                if not visited[nextR][nextC] and graph[nextR][nextC]==1:
                    addNode(nextR,nextC,queue)
    return dangi

# 구분 작업 수행
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0 and not visited[i][j]:
            tempDangi= copy.deepcopy(BFS(i,j))  # 깊은 복사로 해야 주소를 공유하지 않음
            no+=1
            dangiCnt=len(tempDangi)
            dList.append(dangiCnt)


print(len(dList))
dList.sort()
for house in dList:
    print(house)