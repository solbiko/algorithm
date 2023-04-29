"""
1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

visited=[False]*(n+1)
visited[1]=True

# res=list()
# res.append(1)

cnt=0

d = array = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    d[a][b] = 1

# print(d)

def dfs(x):
    global cnt, res
    if x==n:
        # for i in res:
        #     print(i, end=' ')
        # print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if d[x][i] == 1 and not visited[i]:
                visited[i] = True
                # res.append(i)
                dfs(i)
                # res.pop()
                visited[i] = False

dfs(1)
print(cnt)