"""
모든 정점 (i,j) i에서 j로 가는 경로가 있는지 없는지
i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력
"""
import sys

# 인접행렬 크기
n = int(input())

# 인접행렬
d = array = [[sys.maxsize for j in range(n)] for i in range(n)]

# 인접 행렬에 시작 도시와 종료 도시가 같은 자리에 0 저장
for i in range(n):
    d[i][i] = 0

for i in range(n):
    d[i] = list(map(int, input().split()))
print(d)

for k in range(n): # 경유지 k
    for s in range(n):
        for e in range(n):
            if d[s][k] ==1 and d[k][e]==1:
                d[s][e]=1

for i in range(n):
    for j in range(n):
        if d[i][j] != sys.maxsize:
            print(d[i][j], end=" ")
        else:
            print(0, end=" ")
    print()