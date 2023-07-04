def solution(s):
    answer = True
    
    c1=c2=0
    for x in s:
        if x=="(":
            c1+=1
        else:
            c2+=1
            
        if c1-c2<0:
            return False
    
    if c1!=c2:
        answer= False
    
    return answer