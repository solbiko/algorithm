def solution(n, money):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1 # 0원은 아무 동전도 사용하지 않는 경우가 하나 있으므로 1로 초기화

    
    for i in range(len(money)): # 각 동전마다
        for j in range(n+1): # k원까지
            if j-money[i] >= 0:
                dp[j] += dp[j-money[i]]
    return dp[n]