from collections import deque
"""
위상정렬 : 사이클이 없는 방향 그래프에서 노드 순서를 찾는 알고리즘

모든 건물을 짓는데 걸리는 최소 시간
여러 개의 건물을 동시에 지을 수 있음
N개의 건물을 지을 때 각 건물을 짓기 위해 필요한 최소 시간 출력

건물의 종류 수 n(1~500)
각 건물을 짓는 데 걸리느 시간(1~100.000)
건물을 짓기 위해 먼저 지어야 하는 건물들의 번호
각 줄은 -1로 끝남

5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""

# 5
n = int(input())

# 인접 리스트
a = [[] for _ in range(n+1)]
# 진입 차수 리스트
dList = [0] * (n+1)
# 건물 짓는데 걸리는 시간
bList = [0] * (n+1)

# for 건물갯수
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    # 건물 시간 저장
    bList[i] = arr[0]

    j = 1
    while True:
        if arr[j] == -1:
            break
        # 인접 리스트 데이터 저장
        a[arr[j]].append(i)
        # 진입 차수 리스트 추가
        dList[i] += 1
        j += 1

# 정답리스트
rList = [0] * (n+1)

queue = deque()

# dList [0, 0, 1, 1, 2, 1]
for i in range(1, n+1):
    if dList[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()

    for i in a[node]:
        dList[i] -= 1

        # 시간 업데이트
        rList[i] = max(rList[i], rList[node] + bList[node])
        # rList[i] = rList[node] + bList[node]
        print(node, "-", i, rList[node] + bList[node], max(rList[i], rList[node] + bList[node]))

        if dList[i] == 0:
            queue.append(i)


for i in range(1, n+1):
    print(rList[i]+bList[i])