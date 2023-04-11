n = int(input())

list = list(map(int, input().split()))
dp = [0] * n # 최대 연속합
dp[0] = list[0]

for i in range(1, n):
    dp[i] = max(list[i], dp[i-1]+list[i]) # list[i] / 이전최대연속합 + list[i]

print(dp)
print(max(dp))