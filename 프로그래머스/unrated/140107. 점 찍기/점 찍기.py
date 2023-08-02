import math
def solution(k, d):
    answer = 0
    
    for x in range(0, d+1, k):
        y= math.sqrt(d*d - x*x) # 피타고라스
        answer += y//k + 1
    return answer