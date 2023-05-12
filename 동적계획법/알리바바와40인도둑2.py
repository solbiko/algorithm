"""
알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있습니다.
알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다.

계곡의 돌다리는 N×N개의 돌들로 구성되어 있다.
해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다.
현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다.

N*N의 계곡의 돌다리 격자정보가 주어지면 (1,1)격자에서 (N,N)까지 가는데 드는 에너지의 최소량

만약 N=3이고, 계곡의 돌다리 격자 정보가 다음과 같다면
3 2 5
2 3 4
6 5 2
(1, 1)좌표에서 (3, 3)좌표까지 가는데 드는 최소 에너지는 3+2+3+4+2=14이다.

5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4
"""

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]

dp=[[0 for j in range(n)] for i in range(n)]

def dfs(x,y):
    if dp[x][y]>0: # 메모이제이션
        return dp[x][y]

    if x==0 and y==0:
        return arr[0][0]
    else:
        if x==0: # 열 초기화
            dp[x][y]= dfs(x,y-1)+arr[x][y]
        elif y==0: # 행 초기화
            dp[x][y]= dfs(x-1,y)+arr[x][y]
        else:
            dp[x][y]= min(dfs(x-1,y),dfs(x,y-1))+arr[x][y]
        return dp[x][y]

print(dfs(n-1,n-1))