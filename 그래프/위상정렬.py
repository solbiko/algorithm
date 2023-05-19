"""
첫 번째 줄에 전체 일의 개수 N과 일의 순서 정보의 개수 M이 주어집니다.
두 번째 줄부터 M개의 정보가 주어집니다.
6 6
1 4
5 4
4 3
2 5
2 3
6 2

전체 일의 순서를 출력합니다.
1 6 2 5 4 3
"""
import sys
input=sys.stdin.readline
from collections import deque

# 일의개수, 순정보개수
n,m= map(int, input().split())

# 진입 차수 리스트
dList = [0] * (n+1)

# 인접 리스트
a = [[] for _ in range(n+1)]
for i in range(1, m+1):
    s,e=map(int, input().split())
    a[s].append(e)
    dList[e]+=1

queue = deque()

for i in range(1, n+1):
    if dList[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for i in a[node]:
        dList[i]-=1
        if dList[i] == 0:
            queue.append(i)
