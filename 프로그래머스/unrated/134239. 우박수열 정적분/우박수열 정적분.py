def solution(k, ranges):
    answer = [0.0]*len(ranges)
    tmp=[float(k)]
    while k!=1:
        if k%2==1:
            k=k*3+1
        else:
            k/=2
        tmp.append(k)
    
    iList=[]
    for x in range(1, len(tmp)):
        iList.append((tmp[x]+tmp[x-1])/2)
    
    
    for i in range(len(ranges)):
        s, e = ranges[i]
        e=len(iList)+e
        if e-s<0:
            answer[i]=-1.0
        elif s==e:
            answer[i]=0.0
        else:
            val=0
            for x in range(s,e):
                val+=iList[x]
            answer[i]=val
    
    return answer