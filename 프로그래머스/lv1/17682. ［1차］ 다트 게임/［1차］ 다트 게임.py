def solution(dartResult):
    n=''
    temp=[]
    for i in range(len(dartResult)):
        x = dartResult[i]
        
        if x.isdecimal():
            n+=x
        elif x.isalpha():
            j=1
            if x=='D': j=2
            elif x=='T': j=3
            temp.append(int(n)**j)
            n=''
        else:
            if x=='*':
                if len(temp)>1:
                    temp[-2]=temp[-2]*2
                temp[-1]=temp[-1]*2
            elif x=='#':
                temp[-1]=temp[-1]*(-1)
            
    return sum(temp)
