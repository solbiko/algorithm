def solution(name, yearning, photo):
    answer = []
    
    d = {i:j for i,j in zip(name,yearning)}
    
    for x in photo:
        score=0
        for i in x:
            if i in d:
                score+=d[i]
        answer.append(score)
    
    return answer