"""
현수의 위치와 송아 지의 위치가 직선상의 좌표 점으로 주어지면
현수는 현재 위치에서 송아지의 위치까지 앞으로 1, 뒤로 1, 앞으로 5를 이동.
최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지

첫 번째 줄에 현수의 위치 S와 송아지의 위치 E, 직선의 좌표 점은 1부터 10,000 까지이다.

5 14
3
"""
from collections import deque

s,e=map(int, input().split()) # 출발점, 도착점

max=10000 # 좌표 최댓값
visited = [False]*(max+1)
visited[s]=True # 시작점 방문
dist=[0]*(max+1)
dist[s]=0

queue = deque()
queue.append(s)

while queue:
    now = queue.popleft()
    if now==e:
        break
    for next in (now-1, now+1, now+5):
        if 0<next<max and not visited[next]: # 좌표 유효, 미방문
            visited[next]=True
            queue.append(next)
            dist[next]=dist[now]+1

print(dist[e])