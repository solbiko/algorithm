from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()
    p=deque(people)
    
    while p:
        if len(p)==1:
            answer+=1
            break
            
        if p[0]+p[-1]<=limit:
            p.pop()
            p.popleft()
        else:
            p.pop()
            
        answer+=1

    return answer