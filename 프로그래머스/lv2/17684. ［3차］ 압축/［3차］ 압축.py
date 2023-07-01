from string import ascii_uppercase

def solution(msg):
    answer = []
    
    a = {}
    t=1
    for x in ascii_uppercase:
        a[x]=t
        t+=1
       
    w=''
    for x in msg:
        w+=x
        if w not in a:
            a[w]=len(a)+1
            answer.append(a[w[:-1]])
            w = w[-1]
    
    answer.append(a[w])
    
    return answer