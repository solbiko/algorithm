def solution(money):
    dp = [0 for _ in range(len(money))] 
    dp[0] = money[0]
    dp[1] = money[0]
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])


    dp2 = [0 for _ in range(len(money))]
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1])

    return max(max(dp), max(dp2))
