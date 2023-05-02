"""
트리를 구성하는 노드 중 두 노드 사이의 거리가 가장 긴 것
"""
from collections import deque

n=int(input()) # 노드개수
a=[[] for _ in range(n+1)] # 인접리스트
for _ in range(n):
    data=list(map(int, input().split()))
    idx=0
    s=data[idx]
    idx+=1
    while True:
        e=data[idx]
        if e==-1:
            break
        v=data[idx+1]
        a[s].append((e,v))
        idx+=2

d=[0]*(n+1) # 거리리스트
visited=[False]*(n+1)

# 완전 탐색
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v]=True
    while queue:
        nowNode = queue.popleft()
        for i in a[nowNode]:
            nextV=i[0]
            nextW=i[1]
            if not visited[nextV]:
                visited[nextV]=True
                queue.append(nextV)
                d[nextV]=d[nowNode]+nextW

bfs(1)
max=1

for i in range(2,n+1):
    if d[max]<d[i]:
        max=i # 거리 리스트 값중 max값으로 시작점 재설정

d=[0]*(n+1)
visited=[False]*(n+1)
bfs(max)
d.sort()
print(d[n])