import sys
input=sys.stdin.readline

n,l,r=map(int, input().split())
d=[[[0 for k in range(101)] for j in range(101)] for i in range(101)]
d[1][1][1] = 1 # 빌딩이 1개인 경우

for i in range(2, n+1): # 빌딩의 개수
    for j in range(1, l+1): # 왼쪽에서 볼 때
        for k in range(1, r+1): # 오른쪽에서 볼 때
            # 제일 작은 건물을
            # 왼쪽에 놓는 경우의 수(왼쪽에서 보이는거 +1) + 오른쪽에 놓는 경우의 수(오른쪽에서 보이는거 +1) + 가운데 놓는 경우의 수
            d[i][j][k]= d[i-1][j-1][k] + d[i-1][j][k-1] + d[i-1][j][k]*(i-2)

print(d[n][l][r]%1000000007)