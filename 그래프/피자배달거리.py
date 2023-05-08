"""
N×N 크기의 도시지도, 0은 빈칸, 1은 집, 2는 피자집
각 집의 피자배달거리는 해당 집과 도시의 존재 하는 피자집들과의 거리 중 최소값
집과 피자집의 피자배달거리는 |x1-x2|+|y1-y2|

도시에 있는 피자집 중 M개만 살리고 나머지는 폐업
살리고자 하는 피자집 M개를 선택하는 기준으로 도시의 피자배달거리가 최소가 되는 M개의 피자집을 선택

N(2≤N≤50), M(1≤M≤12)
4 4
0 1 2 0
1 0 2 1
0 2 1 2
2 0 1 2
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int, input().split())) for _ in range(n)]
hs=[] # 집
pz=[] # 피자집
cb=[0]*m # 조합의 경우의 수
res=sys.maxsize

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            hs.append((i,j))
        elif graph[i][j]==2:
            pz.append((i,j))


def dfs(x,s):
    # s: 가지를 뻗는 첫번째 수 (for문 시작 숫자)
    global res
    if x==m:
        sum=0 # 도시의 피자거리
        # 각집의 피자배달 거리 구하기
        for j in hs: # 집
            x1=j[0]
            y1=j[1]
            dis=sys.maxsize
            for x in cb:  # 전체 중에 m개 고른 조합 피자집
                x2=pz[x][0]
                y2=pz[x][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
                # print(j, pz[x], dis)
            sum+=dis

        if sum<res:
            res=sum
    else:
        for i in range(s, len(pz)):
            cb[x]=i
            dfs(x+1,i+1)

dfs(0,0)
print(res)