"""
임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산
케빈 베이컨의 수가 가장 작은 사람 구하기

유저수 N(2~100), 친구관계수 M(1~5,000)
친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다
"""
import sys

# 유저수, 친구관계수
n,m = map(int, input().split())

# 인접행렬
d = array = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    d[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    d[a][b]=1
    d[b][a]=1
# print(d)

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if d[s][e] > d[s][k] + d[k][e]:
                d[s][e] = d[s][k] + d[k][e]

min = sys.maxsize
result=-1
for i in range(1, n+1):
    temp=0
    for j in range(1, n+1):
        temp+=d[i][j]
    if temp<min:
        min=temp
        result=i

print(result)