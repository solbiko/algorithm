def solution(cards):
    answer=0
    
    group=[]
    visited=[False]*(len(cards)+1)
    
    for x in cards:
        if not visited[x]:
            temp=[]
            while True:
                if x in temp:
                    break
                temp.append(x)
                visited[x]=True
                x=cards[x-1]
                
            group.append(len(temp))
    
    if len(group)>1:
        group.sort(reverse=True)
        answer = group[0]*group[1]
    
    return answer
    