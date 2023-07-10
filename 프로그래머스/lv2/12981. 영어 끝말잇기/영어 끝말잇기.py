from collections import deque
import math
def solution(n, words):
    answer = []

    q=deque()
    
    for i,x in enumerate(words):
        q.append(((i%n)+1,x))

    cnt=0
    d=set()
    pre=''
    while q:
        cnt+=1
        i,x = q.popleft()
        if pre!='' and pre[-1]!=x[0]:
            return [i, math.ceil(cnt/n)]
        if x in d:
            return [i, math.ceil(cnt/n)]
        else:
            d.add(x)
            pre=x
    return [0,0]