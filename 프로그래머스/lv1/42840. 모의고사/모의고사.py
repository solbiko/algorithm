def solution(answers):
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]

    t1=t2=t3=0
    for i in range(len(answers)):
        if a[i%5]==answers[i]:
            t1+=1
        if b[i%8]==answers[i]:
            t2+=1
        if c[i%10]==answers[i]:
            t3+=1
            
    maxval=max(t1,t2,t3)
    
    answer=[]
    if maxval == t1:
        answer.append(1)
    if maxval == t2:
        answer.append(2)
    if maxval == t3:
        answer.append(3)
    return answer