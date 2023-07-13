def solution(want, number, discount):
    answer = 0
    
    cklist=dict(zip(want, number))
    print(cklist)
    
    def add(x):
        if x in cklist:
            cklist[x]-=1
        else:
            cklist[x]=-1
        
    
    def remove(x):
        if x in cklist:
            cklist[x]+=1
        else:
            cklist[x]=1

    def check():
        flag=True
        for x in cklist:
            if cklist[x]>0:
                flag=False
        return flag
            
            
    n=sum(number)
    for i in range(n):
        add(discount[i])
    if check():
        answer+=1
    
    n=sum(number)
    for i in range(n, len(discount)):
        add(discount[i])
        remove(discount[i-n])
        if check():
            answer+=1
            
    return answer