code = list(map(int, input()))
n = len(code)

dp=[0]*(n+1)
dp[0]=1
dp[1]=1

if code[0] == 0:
    print(0)
else:
    for k in range(1, n):
        i=k+1
        # 1자리
        if code[k] > 0:
            dp[i] += dp[i-1]
        # 2자리
        if 10 <= code[k]+code[k-1]*10 <= 26:
            dp[i] += dp[i-2]
    print(dp[n] % 1000000)