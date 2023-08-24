from math import ceil, floor
def solution(a, b, g, s, w, t):
    answer = -1
    
    def count(time):
        gold=0
        silver=0
        weight=0
        
        for i in range(len(g)):
            tmp=floor(time/t[i])
            deliver=tmp//2+tmp%2
            
            gold+=min(g[i], w[i]*deliver) # 가지고 있는 골드, 트럭 용량 작은 값
            silver+=min(s[i], w[i]*deliver) # 가지고 있는 실버, 트럭 용량 작은 값
            weight+=min(g[i]+s[i], w[i]*deliver) 
        
        if gold>=a and silver>=b and weight>=a+b:
            return True
        else:
            return False
    
    l=0
    r=(a+b)*max(t)*2
    while l<r:
        mid=(l+r)//2
        if count(mid):
            answer=mid
            r=mid
        else:
            l=mid+1
    
    return answer