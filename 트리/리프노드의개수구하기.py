"""
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.트리가 주어졌을 때, 노드 하나를 지울 것이다.
그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

첫째 줄에 트리의 노드의 개수N(1~50)
둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다.
셋째 줄에는 지울 노드의 번호가 주어진다.
5
-1 0 0 1 1
2

입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.
"""
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
parent=list(map(int, input().split()))
deleteNode=int(input())

tree = [[] for _ in range(n)]
root=0
for i in range(n):
    if parent[i]!=-1:
        tree[parent[i]].append(i)
        tree[i].append(parent[i])
    else:
        root=i

visited = [False]*(n+1)

cnt=0

def dfs(v):
    global cnt
    visited[v] = True
    cNode=0
    for i in tree[v]:
        if not visited[i] and i!=deleteNode:
            cNode+=1
            dfs(i)
    if cNode==0:
        cnt+=1


if deleteNode==root:
    print(0)
else:
    dfs(root)
    print(cnt)