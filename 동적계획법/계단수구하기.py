import sys
input=sys.stdin.readline

# 길이
n=int(input())

# dp[계단길이][계단높이]
dp=[[0 for j in range(11)] for i in range(n+1)]

for i in range(1, 10):
    dp[1][i]=1 # 길이가 1일땐 모든 경우의수 1

for i in range(2,n+1):
    dp[i][0]=dp[i-1][1] # 0인경우 뒤에 1만 올 수 있음
    dp[i][9]=dp[i-1][8] # 9인경우 뒤에 8만 올 수 있음
    for j in range(1,9): #1~9인경우 인접수(+-1)
        print(j)
        dp[i][j]= dp[i-1][j-1] + dp[i-1][j+1]

# print(dp[n])

sum=0
for i in range(10):
    sum=(sum+dp[n][i])

print(sum%1000000000)