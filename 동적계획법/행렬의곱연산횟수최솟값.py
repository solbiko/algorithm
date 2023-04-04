import sys
imput=sys.stdin.readline

# 행렬의 갯수
n=int(input())
# 행렬
m=[]
# 최소 연산 횟수 저장 리스트
d=[[-1 for j in range(n+1)] for i in range(n+1)]

m.append((0,0))

for _ in range(n):
    x,y=map(int, input().split())
    m.append((x,y))

def execute(s,e):
    result=sys.maxsize

    if d[s][e] != -1: # 이미 계산
        return d[s][e]
    if s==e: # 행렬 1개
        return 0
    if s+1==e: # 행렬 2개
        return m[s][0]*m[s][1]*m[e][1]

    for i in range(s,e):
        result=min(result, m[s][0] * m[i][1] * m[e][1] + execute(s,i) + execute(i+1,e))
    d[s][e]=result
    return d[s][e]


print(execute(1,n))
