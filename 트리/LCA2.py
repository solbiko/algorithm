"""
두 노드 쌍 M개 LCA 구하기

노드의 개수 N(2~100,000)
N-1줄 트리상 연결된 두 노드
가장 가까운 공통 조상을 알고 싶은 쌍의 개수 M(1~100,000)
M줄 노드쌍

일반적인 LCA구하기 -> 시간초과
제곱수 형태를 이용한 빠르게 최소 공통 조상 구하기

"""

import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

# 수의 개수
N = int(input())

# 트리 데이터 저장
tree = [[0] for _ in range(N + 1)]

for _ in range(0, N - 1):
    # 인접 리스트에 트리 데이터 저장
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# 노드 깊이 리스트
depth = [0] * (N + 1)

# 방문체크 저장 리스트
visited = [False] * (N + 1)

temp = 1
kmax = 0 # 최대 가능 높이
while temp <= N:
    temp <<= 1 # 변수의 값을 왼쪽으로 지정된 비트 수 만큼 이동,  n << m : n * 2의 m승
    kmax += 1

# 노드 조상 리스트
parent = [[0 for j in range(N + 1)] for i in range(kmax + 1)]

def BFS(node):
    queue = deque()

    # 큐 자료구조에 출발 노드 넣기
    queue.append(node)

    # 현재 노드 방문 기록
    visited[node] = True

    level = 1 # 트리 깊이
    now_size = 1 # 현재 깊이에서 트리 크기

    count = 0
    while queue:

        # 큐에서 노드 데이터 가져오기
        now_node = queue.popleft()

        for next in tree[now_node]: # 현재 노드와 연결된 노드 탐색
            if not visited[next]:
                visited[next] = True
                # 큐에 데이터 삽입
                queue.append(next)
                # 부모 노드 저장
                parent[0][next] = now_node
                # 노드 현재 깊이 저장
                depth[next] = level

        count += 1
        if count == now_size: # 현재 깊이의 모든 노드 방문
            count = 0
            # 바로 아래 단계 트리 노드 개수 저장
            now_size = len(queue)
            # 현재 depth 1 wmdrk
            level += 1


BFS(1) # 깊이와 부모 노드 저장

for k in range(1, kmax + 1): # 2^k번째 부모 노드 계산 및 저장
    for n in range(1, N + 1): # 노드 개수만큼 반복
        # 점화식
        parent[k][n] = parent[k - 1][parent[k - 1][n]]


def LCA(a, b):
    if depth[a] > depth[b]:  # 더 깊은 depth가 b가 되도록
        temp = a
        a = b
        b = temp

    # 두 노드의 depth 맞추기
    for k in range(kmax, -1, -1):
        if pow(2, k) <= depth[b] - depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]

    # 두 노드의 같은 조상이 나올 때까지 각 노드를 부모 노드로 변경
    for k in range(kmax, -1, -1):
        if a == b: break
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    LCA = a
    if a != b:
        LCA = parent[0][LCA]
    return LCA

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(str(LCA(a, b)))
    print("\n")