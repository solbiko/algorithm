from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    infoDict={}
    for x in info:
        xl = x.split(" ")
        info_key=xl[:-1]
        score =int(xl[-1])
        
        for i in range(5):
            for c in combinations(info_key, i):
                key = "".join(c)
                if key in infoDict:
                    infoDict[key].append(score)
                else:
                    infoDict[key]=[score]
                    
    for k in infoDict:
        infoDict[k].sort()
    
    for q in query:
        q = q.replace("and", "")
        q = q.replace("-", "")
        q = q.split()
        qkey = ''.join(q[:-1])
        qscore = int(q[-1])

        if qkey in infoDict:
            tlist = infoDict[qkey]
            if tlist:
                idx = bisect_left(tlist, int(qscore))
                answer.append(len(tlist)-idx)
        else:
            answer.append(0)
    
    
    return answer