"""
같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.
상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산
이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.
R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.
입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다.
몇연쇄가 되는지 출력
'"""
import sys
from collections import deque
input=sys.stdin.readline
field=[list(input().strip()) for _ in range(12)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
# print(field)

"""
1. bfs로 찾는 함수
2. 밑으로 내리는 함수
3. 카운트
"""
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    temp.append((x,y))
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0<=nx<12 and 0 <=ny<6 and field[nx][ny] == field[x][y] and not visited[nx][ny]:
                queue.append((nx, ny))
                temp.append((nx, ny))
                visited[nx][ny] = True

def down():
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11,j,-1):
                if field[j][i] != "." and field[k][i] == ".":
                    field[k][i] = field[j][i]
                    field[j][i] = "."
                    break


cnt=0
while True:
    flag=True
    visited = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j]!='.' and not visited[i][j]:
                visited[i][j]=True
                temp=[]
                bfs(i,j)
                if len(temp)>=4:  # 지우기
                    flag=False
                    for x, y in temp:
                        field[x][y] = "."
    if flag:
        break
    down()
    cnt+=1


print(cnt)