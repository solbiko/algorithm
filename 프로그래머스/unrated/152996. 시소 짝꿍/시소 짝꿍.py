from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)
    for k,v in counter.items():
        c=counter[k]
        answer += c*(c-1)//2
        answer += c*counter[k*3/2]
        answer += c*counter[k*2]
        answer += c*counter[k*4/3]

    return answer