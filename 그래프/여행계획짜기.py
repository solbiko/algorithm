"""
유니온파인드

도시 N개
경로 M개
N개의 정수 도시의 연결 정보
마지막 줄 여행 계획

A-B, B-C, A-D, B-D, E-A
여행계획 ECBCD
E-A-B-C-B-C-B-D

여행계획에 속한 도시들이 순서대로 주어졌을 때 게획대로 여행이 가능한지 판별
"""

n=int(input())
m=int(input())

# 도시연결 인접행렬
graph=[[0 for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    graph[i]= list(map(int, input().split()))
    # index 1부터 시작이기 때문에 0번째에 0데이터 삽입 필요
    graph[i].insert(0, 0)
# print(graph)

# 여행 계획 리스트
route = list(map(int, input().split()))
# index 1부터 시작이기 때문에 0번째에 0데이터 삽입 필요
route.insert(0, 0)
# print(route)

# 대표노드  리스트
arr=[0]*(n+1)
for i in range(1, n+1):
    arr[i]=i

def find(a): # 대표노드 찾기
    if a == arr[a]:
        return a
    else:
        arr[a] = find(arr[a])
        return arr[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        arr[b] = a

# 인접행렬 탐색
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 1:
            union(i,j)


index=find(route[1])
isConnect=True
# route에 포하되는 노드들의 대표 노드가 모두 동일한지 확인
for i in range(2, len(route)):
    if index!= find(route[i]):
        isConnect=False
        break

print("YES" if isConnect else "NO")

