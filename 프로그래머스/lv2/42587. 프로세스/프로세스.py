def solution(priorities, location):
    q = [(p,i) for i,p in enumerate(priorities)]

    cnt=0
    while True:
        p= q.pop(0)

        if any(p[0] < x[0] for x in q):
            q.append(p)
        else:
            cnt+=1
            if p[1] == location:
                return cnt