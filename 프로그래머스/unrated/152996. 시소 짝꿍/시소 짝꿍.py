from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)
    for c in counter:
        answer += counter[c]*(counter[c]-1)//2
        answer += counter[c]*counter[c*3/2]
        answer += counter[c]*counter[c*2]
        answer += counter[c]*counter[c*4/3]

    return answer