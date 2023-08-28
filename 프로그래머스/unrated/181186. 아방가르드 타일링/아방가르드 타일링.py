import sys
sys.setrecursionlimit(10**6)
dp=[0]*100001

def solution(n):
    
    def block(n):
        answer = 0
 
        if n==1:
            dp[1]=1
            return 1
        if n==2:
            dp[2]=3
            return 3
        if n==3:
            dp[3]=10
            return 10
        if n==4:
            dp[4]=23
            return 23
        if n==5:
            dp[5]=62
            return 62
        if n==6:
            dp[6]=170
            return 170
        
        if dp[n-1]:
            answer+=dp[n-1]
        else:
            answer += block(n-1)
        if dp[n-2]:
            answer += dp[n-2]*2
        else:
            answer += block(n-2)*2
        if dp[n-3]:
            answer += dp[n-3]*6
        else:
            answer += block(n-3)*6
        if dp[n-4]:
            answer += dp[n-4]*1
        else:
            answer += block(n-4)*1
        if dp[n-6]:
            answer -= dp[n-6]*1
        else:
            answer -= block(n-6)*1
        
        dp[n]=answer
        return answer

    return block(n) % 1000000007
    
  