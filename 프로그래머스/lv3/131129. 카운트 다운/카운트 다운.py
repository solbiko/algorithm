"""
1. 가장 먼저 0점을 만든 선수가 승리
2. "싱글" 또는 "불"을 더 많이 던진 선수가 승리
3. 선공인 선수가 승리

최선의 경우 던질 다트 수와 그 때의 "싱글" 또는 "불"을 맞춘 횟수(합)
"""

import sys
def solution(target):
    
    n = max(61, target+1)
    
    d = [[target, 0] for _ in range(n)]  # 조합수, single or bool 개수
    
    d[50] = [1, 1]
    
    for i in range(1, 21):
        if 1<=i<= 20:
            d[i]=[1, 1]
        if d[i*2] == [target, 0]:
            d[i*2] = [1, 0]
        if d[i*3] == [target, 0]:
            d[i*3] = [1, 0] 
    
    for i in range(23, n):
        single = []
    
        for j in range(1, 61):
            if d[i-j][0] + d[j][0] <= d[i][0]:
                d[i][0] = d[i-j][0] + d[j][0]
                single.append([d[i-j][0] + d[j][0], d[i-j][1] + d[j][1]])
        
        single.sort(key=lambda x: [x[0], -x[1]])
        
        if len(single) > 0:
            d[i] = single[0]
            
    return d[target]

