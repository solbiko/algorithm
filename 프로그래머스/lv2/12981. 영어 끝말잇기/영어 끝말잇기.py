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


def solution2(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: 
            return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]