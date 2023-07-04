def solution(n, times):
    answer = 0
    
    # 이분탐색
    l=1
    r=max(times)*n # 가장 오래 걸리는 심사관에게 전부 심사하는 경우
    
    while l<=r:
        mid=(l+r)//2
        
        people=0 # 모든 심사관들이 mid분동안 심사한 사람의 수
        for time in times:
            people+=mid//time
            if people>=n:
                break
                
        if people>=n:
            answer=mid
            r=mid-1
        else:
            l=mid+1
            
    return answer