def solution(n):
    answer = 0
    
    cnt=bin(n)[2:].count('1')
    n+=1
    
    while True:
        if cnt == bin(n)[2:].count('1'):
            answer=n
            break
        else:
            n+=1
    
    return answer