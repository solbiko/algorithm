"""
N(2 ≤ N ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다.
트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.
두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다.
그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.
"""
import sys
input = sys.stdin.readline

n = int(input())  # 수의 개수
tree = [[] for _ in range(n+1)]  # 트리 데이터 저장
for _ in range(0, n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth=[0]*(n+1)  # 노드 깊이 리스트
parent = [0]*(n+1) # 노드 조상 리스트
visited=[False]*(n+1)  # 방문체크 저장 리스트

def BFS(node):
    queue = [node]
    visited[node] = True  # 현재 노드 방문 기록
    while queue:
        # 큐에서 노드 데이터 가져오기
        now_node = queue.pop(0)
        for next in tree[now_node]:  # 현재 노드와 연결된 노드 탐색
            if not visited[next]:
                visited[next] = True
                queue.append(next)  # 큐에 데이터 삽입
                parent[next] = now_node  # 부모 노드 저장
                depth[next] = depth[now_node] + 1  # 노드 depth 저장

BFS(1) # 깊이와 부모 노드 저장

def LCA(a, b):
    if depth[a] < depth[b]: # a노드가 더 작으면 swap, 더 깊은 depth가 a가 되도록
        temp =a
        a=b
        b=temp
    while depth[a]!=depth[b]:  # depth 맞추기
        a=parent[a]
    while a!=b: # 공통조상찾기
        a=parent[a]
        b=parent[b]

    return a

m=int(input())
mydict = dict()
for _ in range(m):
    a, b = map(int, input().split())
    if not mydict.get((a, b), 0): #같은 질문일 경우 재계산을 하지 않기 위해 딕셔너리 자료형 사용
        mydict[(a, b)] = mydict[(b, a)] = LCA(a, b)
    print(mydict.get((a, b)))