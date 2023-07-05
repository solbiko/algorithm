def solution(scores):
    answer = 0
    
    w=scores[0]
    scores.sort(key=lambda x:(-x[0], x[1]))
    
    maxval=0
    
    for i,j in scores:
        if w[0]<i and w[1]<j:
            return -1
        
        if maxval<=j: # 정렬했기 때문에 j만 보면 됨
            maxval=j
            if i+j> w[0]+w[1]:
                answer+=1
                
    return answer+1