"""
첫째 줄에는 정점수 n(2~20), 간선수 m
m줄 연결정보와 거리비용
6 9
1 2 7
1 3 4
2 1 2
2 3 5
2 5 5
3 4 5
4 2 2
4 5 5
6 4 5
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = [[0 for j in range(n)] for i in range(n)]

for i in range(m):
    a, b, w = map(int, input().split())
    d[a-1][b-1]= w
print(d)

for i in range(n):
    for j in range(n):
        print(d[i][j], end=" ")
    print()


