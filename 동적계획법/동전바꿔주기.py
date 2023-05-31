"""
입력으로 지폐의 금액 T
동전의 가지 수 k
각 동전 하나의 금액 pi와 개수 ni가 주어질 때 (i=1, 2,…, k)

지폐를 동전으로 교환하는 방법의 가지 수
"""
t=int(input()) # 지폐금액
k=int(input()) # 동전가지수
coins=[(0,0)]
for i in range(k):
    pi,ni=map(int, input().split())
    coins.append((pi,ni))

# dp[i][j] : i번째 동전까지 사용해서 j원을 만들 수 있는 경우의 수
dp = [[0 for _ in range(t+1)] for _ in range(k+1)]
dp[0][0] = 1 # 0원은 아무 동전도 사용하지 않는 경우가 하나 있으므로 1로 초기화

for i in range(1, k+1): # 각 동전마다
    val, cnt = coins[i]
    for j in range(t+1): # T원까지
        dp[i][j] = dp[i-1][j]
        for v in range(1, cnt+1):# 동전 갯수만큼 반복
            if j-v*val >= 0:
                dp[i][j] += dp[i-1][j-v*val]
            else:
                break
print(dp[k][t])