def solution(routes):
    answer=1

    routes.sort()

    s=routes[0][0]
    e=routes[0][1]
    
    for i in range(1,len(routes)):
        ns,ne=routes[i]
        if e>=ns: 
            e = min(e, ne)
        else:
            answer+=1
            s,e=ns,ne
        print(s,e)
    return answer