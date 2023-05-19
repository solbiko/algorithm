"""
입력으로 지폐의 금액 T
동전의 가지 수 k
각 동전 하나의 금액 pi와 개수 ni가 주어질 때 (i=1, 2,…, k)

지폐를 동전으로 교환하는 방법의 가지 수
"""
t=int(input()) # 지폐금액
k=int(input()) # 동전가지수
coin=[(0,0)]
for i in range(k):
    pi,ni=map(int, input().split())
    coin.append((pi,ni))

dp = [[0 for _ in range(t+1)] for _ in range(k+1)]
dp[0][0] = 1

for i in range(1, k+1): # 각 동전마다
    val, cnt = coin[i]
    for j in range(t+1): # T원까지
        dp[i][j] = dp[i-1][j]
        for v in range(1, cnt+1):# 동전 갯수만큼 반복
            if j-v*val >= 0:
                dp[i][j] += dp[i-1][j-v*val]
            else:
                break

print(dp[k][t])