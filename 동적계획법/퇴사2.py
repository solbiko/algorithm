# top down
n = int(input())

dp = [0]*(n+2) # 오늘부터 퇴사일까지 벌수있는 최대수입 (점화식 테이블) 
t=[0]*(n+1) # 상담에 필요한 일수
p=[0]*(n+1) # 상담 완료시 수입 저장

for i in range(1,n+1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):
    if i + t[i] > n+1: # 상담에 걸리는 시간이 퇴사전에 끝나는지
         dp[i] = dp[i+1] # 안끝남, 그대로
    else: # 끝남
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]]) 
        # i+1일~ 퇴사일 최대수입, i번째 상담비용+i번째 상담이 끝난 다음 날~ 퇴사일 최대 수입

print(dp[1])