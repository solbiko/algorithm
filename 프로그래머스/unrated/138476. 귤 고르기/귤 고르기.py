from collections import Counter

def solution(k, tangerine):
    answer=0

    d=Counter(tangerine)
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)

    if len(d)==1:
        return 1

    else:
        sum=0
        for i in range(len(d)):
            if k>sum:
                sum += d[i][1]
                answer+=1
            else:
                break

    return answer