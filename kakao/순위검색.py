from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []

    infoDict = {}
    for x in info:
        xl = x.split(" ")
        info_key = xl[:-1]
        score = int(xl[-1])

        for i in range(5):
            for c in combinations(info_key, i):
                key = "".join(c)
                if key in infoDict:
                    infoDict[key].append(score)
                else:
                    infoDict[key] = [score]

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
                answer.append(len(tlist) - idx)
        else:
            answer.append(0)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
           ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))