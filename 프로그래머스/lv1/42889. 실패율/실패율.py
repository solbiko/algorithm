def solution(N, stages):
    answer = []
    
    a=[0]*(N+1)
    for x in stages:
        a[x-1]+=1
    print(a)

    
    b={}
    for i in range(N):
        if sum(a[i:])!=0:
            b[i+1]=a[i]/sum(a[i:])
        else:
            b[i+1]=0
    
    print(b)

    b = sorted(b.items(), key=lambda x: x[1], reverse=True)
    print(b)
    
    for x in b:
        answer.append(x[0])

    return answer