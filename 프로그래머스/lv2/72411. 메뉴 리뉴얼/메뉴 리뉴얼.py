from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        temp=[]
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
            
        cnt = Counter(temp)
        if len(cnt)>1:
            m=max(cnt.values())
            for i in cnt:
                if cnt[i]>=2 and cnt[i]==m:
                    answer.append("".join(i))
                    answer.sort()
        
    
    return answer