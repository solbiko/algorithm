"""
임계경로 구하기

1분도 쉬지않고 달려야 하는 사람들이 지나는 도로의 수
: 가장 오랜 시간이 걸리는 사람 → 임계경로, 그에 속한 정점구하기

에지 뒤집기
"""

import sys
from collections import deque
input=sys.stdin.readline

n=int(input()) # 도시 수
m=int(input()) # 도로 수
a=[[] for _ in range(n+1)] # 도시 인접 리스트
reverseA=[[] for _ in range(n+1)] # 역방향 인접 리스트
d=[0]*(n+1) # 진입 차수 리스트

for i in range(m):
    s,e,v=map(int, input().split())
    a[s].append((e,v)) # 인접 리스트 데이터 저장
    reverseA[e].append((s,v)) # 역방향 인접 리스트 데이터 저장
    d[e]+=1 # 진입 차수 리스트 저장

# 시작도시, 도착도시
start,end= map(int,input().split())

# 큐 생성
queue=deque()
queue.append(start) # 출발 도시 큐에 삽입

result=[0]*(n+1)

# 위상정렬 수행
while queue:
    now=queue.popleft() # 큐에서 데이터 가져오기
    for i in a[now]: # 현재 노드에서 갈 수 있는 노드 탐색
        next = i[0]
        value = i[1]
        d[next]-=1 # 타깃노드 진입 차수 -1
        result[next]=max(result[next], result[now]+value)
        if d[next]==0:
            queue.append(next)

resultCnt=0 # 1분도 쉬지않고 달려야 하는 도로의 개수
visited=[False]*(n+1) # 각 도시 방문 유무


# 도착 도시에서 역방향으로 위상정렬 수행
queue.clear()
queue.append(end)
visited[end]=True

while queue:
    now=queue.popleft() # 큐에서 데이터 가져오기
    # 역방향 인접리스트
    for i in reverseA[now]: # 현재 노드에서 갈 수 있는 노드 개수
        next = i[0]
        value = i[1]
        if result[next]+value==result[now]:
            # 1분도 쉬지않고 달려야 하는 도로 값 +1
            resultCnt+=1
            if not visited[next]:
                visited[next]=True
                queue.append(next)


print(result[end])
print(resultCnt)

