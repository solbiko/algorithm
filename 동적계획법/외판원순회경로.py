import sys
imput=sys.stdin.readline

# 도시개수
n=int(input())
# 비용 행렬
w=[]

for i in range(n):
    w.append([])
    w[i]=list(map(int,input().split()))

d=[[0 for j in range(1 << 16)] for i in range(16)] # n(1~16)

def tsp(c,v):
    if v==(1<<n)-1: # 모든노드 방문
        if w[c][0] ==0: # 시작도시로 들어갈 수 없음
            return float('inf')
        else:
            return w[c][0]

    if d[c][v]!=0: # 이미방문
        return d[c][v]

    res = float('inf')
    for i in range(0,n):
        if (v &(1<<i))==0 and w[c][i]!=0:  # 방문한 적없고, 갈수 있는 도시
            res = min(res, tsp(i, (v | (1<<i))) +w[c][i])
    d[c][v] = res
    return d[c][v]

print(tsp(0,1))



