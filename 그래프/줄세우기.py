"""
위상정렬

학생수 n, 키비교횟수 m
키 비교한 두 학생 번호(1~n) A,B : A가 B 앞에 서야함
"""
from collections import deque

# 노드(학생수) n, 엣지(키비교횟수) m
n,m=map(int,input().split())

# 진입차수리스트
d = [0] * (n+1)

# 인접 리스트
a = [[] for _ in range(n+1)]
for _ in range(m):
    s,e=map(int,input().split())
    a[s].append(e) # 인접 리스트 데이터 저장
    d[e]+=1 # 진입차수 데이터 저장

queue = deque()

# 진입 차수 리스트의 값이 0인 노드 큐에 삽입
for i in range(1,n+1):
    if d[i]==0:
        queue.append(i)

while queue: # 위상 정렬 수행
    now=queue.popleft() # 큐에서 데이터 가져오기
    print(now, end=' ') # 현재 노드값 출력
    for next in a[now]: # 현재 노드에서 갈 수 있는 노드의 개수
        d[next]-=1 # 타깃 노드 징입 차수 리스트값 -1
        if d[next]==0: # 타깃노드 진입차수 0이면 큐에 타깃 노드 추가
            queue.append(next)