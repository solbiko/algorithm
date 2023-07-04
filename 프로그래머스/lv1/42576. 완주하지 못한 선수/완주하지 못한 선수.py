from collections import Counter
def solution(participant, completion):

    dic1=Counter(participant)
    dic2=Counter(completion)

    answer=dic1-dic2
    return list(answer.keys())[0]