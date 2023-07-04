from collections import Counter
def solution(participant, completion):

    dic1=Counter(participant)
    dic2=Counter(completion)

    for x in dic1:
        if dic1[x]-dic2[x]!=0:
            return x
