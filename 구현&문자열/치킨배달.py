"""
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
N개의 줄에는 도시의 정보, 0은 빈 칸, 1은 집, 2는 치킨집
집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int, input().split())) for _ in range(n)]

house=[]  # 집
chicken=[]  # 치킨집
cb=[0]*m  # 조합의 경우의 수

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            house.append((i,j))
        elif graph[i][j]==2:
            chicken.append((i,j))

res=sys.maxsize


def dfs(x,cnt):
    global res

    if x==m:  # m개를 골랐으면
        sum=0  # 도시의 치킨 거리
        # 각집의 치킨 배달 거리 구하기
        for x1,y1 in house:  # 집
            dis=sys.maxsize

            # 전체 중에 m개 고른 조합 치킨집
            for c in cb:
                x2 = chicken[c][0]
                y2 = chicken[c][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum<res:
            res=sum
    else:
        for i in range(cnt, len(chicken)):  # 치킨 집 선택
            cb[x]=i  # 치킨집 인덱스
            dfs(x+1,i+1)

dfs(0,0)
print(res)