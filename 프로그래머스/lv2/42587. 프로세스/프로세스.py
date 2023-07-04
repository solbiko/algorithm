from collections import deque

def solution(priorities, location):
    q=deque()

    for i in range(len(priorities)):
        x=priorities[i]
        q.append((x,i))

    cnt=0
    while q:
        p= q.popleft()

        flag=False
        for i in q:
            if p!=i and i[0]>p[0]:
                flag=True
                break

        if flag:
            q.append(p)
        else:
            cnt+=1
            if p[1] == location:
                return cnt