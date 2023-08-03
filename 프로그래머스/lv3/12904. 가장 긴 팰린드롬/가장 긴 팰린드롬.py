def solution(s):
    answer = 0
    
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if j - i < answer: 
                break
                
            x=s[i:j]
            if x == x[::-1]:
                answer=j-i
                break
            
    return answer