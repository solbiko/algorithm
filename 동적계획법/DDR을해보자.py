import sys
input=sys.stdin.readline

# N개의 열, L 왼발, R 오른발
dp=[[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]

"""
한 발을 이동할 때 드는 힘 미리 저장
mp[1][2] = 1에서 2로 이동할 때 드는 힘
- 같은 지점 한번 더 1
- 0에서 이동 2
- 인접 지점 3
- 반대편 4
"""
mp=[[0,2,2,2,2],
    [2,1,3,4,3],
    [2,3,1,3,4],
    [2,4,3,1,3],
    [2,3,4,3,1]]

s=1
dp[0][0][0]=0

l=list(map(int, input().split()))
idx=0

while l[idx]!=0:
    n=l[idx]

    # 오른발로 이동해 현재 다리 위치로 만들수 있는 경우의 수
    for i in range(5):
        if n==i: # 두발이 같은 자리
            continue
        for j in range(5):
            dp[s][i][n]=min(dp[s-1][i][j]+mp[j][n], dp[s][i][n])

    # 왼발로 이동해 현재 다리 위치로 만들수 있는 경우의 수
    for j in range(5):
        if n == j:  # 두발이 같은 자리
            continue
        for i in range(5):
            dp[s][n][j] = min(dp[s-1][i][j] + mp[i][n], dp[s][n][j])

    s+=1
    idx+=1

s-=1 # 마지막 이동 횟수로 idx 조정
result=sys.maxsize

for i in range(5):
    for j in range(5):
        result=min(result, dp[s][i][j])

print(result)
