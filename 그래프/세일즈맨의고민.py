"""
도시수 n(1~100), 시작, 종료, 교통수단 m(1~100)
교통 수단 정보 : 시작 끝 가격
각 도시에서 벌 수 있는 돈의 최댓값(0~1,000,000)

같은 도시 여러번 방문 가능
버는 돈보다 쓰는 돈이 많다면 도착 도시에 도착할때 지니고 있는 돈의 액수가 음수

* 도착도시에 도착할 때 지니고 있는 돈의 최대 액수
도착 불가 'gg'
무한 'Gee'
"""

import sys
input=sys.stdin.readline

# 도시수 n(1~100), 시작, 종료, 교통수단 m(1~100)
n,s,e,m=map(int, input().split())
graph = [] # 교통 수단 정보, 에지 리스트
d = [-sys.maxsize]*n # 최단 경로 리스트

# 교통 수단 정보, 에지 리스트
for _ in range(m):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))

# 각 도시에서 벌 수 있는 돈의 최댓값
mList=list(map(int,input().split()))

d[s] = mList[s]
# 변형 벨만-포드
for i in range(n+101):
    for start, end, price in graph:
        if d[start]==-sys.maxsize: # 출발노드 미방문 노드
            continue
        elif d[start]==sys.maxsize: # 출발노드가 양수 사이클에 연결된 노드
            d[end]=sys.maxsize
        elif d[end] < d[start]+mList[end]-price: # 종료노드값 < 출발노드값+도착도시수입+에지가중치
            d[end]=d[start]+mList[end]-price

            # 에지 사용 횟수가 n-1을 넘어선 이후 갱신되면 양수 사이클에 연결되어 있다는 의미
            # 종료노드를 양수 사이클 연결 노드로 업데이트
            if i >= n-1:
                d[end]=sys.maxsize

if d[e] == -sys.maxsize: # 도착 불가능
    print("gg")
elif d[e]==sys.maxsize: # 양수싸이클, 무한대
    print("Gee")
else:
    print(d[e])
