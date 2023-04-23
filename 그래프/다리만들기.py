"""
모든 섬을 연결하는 다리의 최솟값

1. 주어진 지도에서 섬으로 표현된 값을 각각의 섬마다 다르게 표현
    - 지도의 정보를 2차원 리스트에 저장하고 섬으로 표시된 모든 점에서 BFS를 실행해 섬을 구분
2. 섬의 모든 위치에서 다른섬으로 연결할 수 있는 에지가 있는지 확인해 에지 리스트 만들기
    - 다리를 지어 다른 섬으로 연결 할 수 있는지 확인
    - 연결할 곳이 현재 섬이면 탐색 중단, 바다라면 계속 수행
    - 다른 섬을 만났을 때 다리의 길이가 2 이상히면 에지 리스트에 추가
3. 최소신장트리
    - 에지를 오름차순으로 정렬해 최소신장리 알고리즘 수행
"""
import copy
import sys
from collections import deque
from queue import PriorityQueue
input=sys.stdin.readline

# 네 방향 탐색을 위한 상수 → ↓ ← ↑
dr=[0,1,0,-1]
dc=[1,0,-1,0]

n,m=map(int,input().split()) # 행렬의 크기
myMap=[[0 for j in range(m)] for i in range(n)] # 맵 정보 저장 리스트
visited= [[False for j in range(m)] for i in range(n)] # BFS 시 방문 여부 저장 리스트

for i in range(n):
    myMap[i] = list(map(int, input().split()))

sNum=1 # 섬번호
sumList=list([]) # 모든 섬 정보 이중리스트
mList=[] # 1개의 섬 정보리스트

# 섬에 한칸을 더해주는 함수
def addNode(i,j,queue):
    myMap[i][j]=sNum # 섬 번호 저장
    visited[i][j]=True # 방문 표시
    mList.append([i,j]) # 섬 정보에 해당 노드 추가
    queue.append([i,j]) # BFS를 위한 큐에 해당 노드 추가

def BFS(i,j):
    queue=deque()
    mList.clear()
    start=[i,j]
    queue.append(start)
    mList.append(start)
    visited[i][j]=True
    myMap[i][j]=sNum

    while queue:
        # print(queue)
        r,c=queue.popleft()
        for d in range(4):
            tempR=dr[d]
            tempC=dc[d]
            nextR= r+tempR
            nextC= c+tempC
            while nextR >=0 and nextR<n and nextC>=0 and nextC<m: # 지도 격자
                if not visited[nextR][nextC] and myMap[nextR][nextC] !=0:
                    # 연결된 새로운 노드가 확인되면 저장
                    addNode(nextR, nextC, queue)
                else:
                    break
                if tempR<0:
                    tempR-=1
                elif tempR>0:
                    tempR+=1
                elif tempC<0:
                    tempC-=1
                elif tempC>0:
                    tempC+=1

    return mList

# 섬 구분 작업 수행
for i in range(n):
    for j in range(m):
        if myMap[i][j] != 0 and not visited[i][j]:
            # BFS를 실행해 하나의 섬 정보 가져오기
            tempList = copy.deepcopy(BFS(i,j))  # 깊은 복사로 해야 주소를 공유하지 않음
            sNum+=1
            sumList.append(tempList)

pq= PriorityQueue()

# 모든 섬에서 지을 수 있는 다리를 찾고 저장
# 섬의 각 지점에서 만들 수 있는 모든 에지를 저장
for now in sumList:
    # 1개의 섬 정보
    for temp in now:
        # 1개의 섬의 모든 위치에서 만들 수 있는 다리 정보 저장
        r=temp[0]
        c=temp[1]
        now_sum=myMap[r][c]
        for d in range(4): # 네방향 탐색, 우선순위 큐에 에지 정보 저장
            tempR=dr[d]
            tempC=dc[d]
            blength=0 # 다리길이
            while r + tempR >= 0 and r + tempR < n and c + tempC >= 0 and c + tempC < m:  # 지도 격자
                if myMap[r + tempR][c + tempC]== now_sum: # 같은 섬이면 에지 만들수 없음
                    break
                elif myMap[r + tempR][c + tempC] !=0: # 바다 X, 다른 섬
                    if blength>1: # 길이가 1이상
                        pq.put((blength, now_sum, myMap[r + tempR][c + tempC]))
                    break
                else: # 바다, 다리길이 연장
                    blength+=1
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1

# 유니온파인드
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

arr = [0] * sNum
for i in range(len(arr)):
    arr[i] = i

useEdge = 0 # 사용 에지 수 저장 변수
result = 0 # 정답 변수

# MST 알고리즘 수행
while pq.qsize()>0:
    # 큐에서 에지 정보 가져오기
    v, s, e = pq.get()

    # 에지 시작점과 끝점의 부모 노드가 다르면 (연결해도 사이클이 생기지 않으면)
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

if useEdge == sNum -2: # sNum이 실제 섬의 수보다 1크기 때문에 섬의 번호 표시를 위해 -2연산
    print(result)
else:
    print(-1)