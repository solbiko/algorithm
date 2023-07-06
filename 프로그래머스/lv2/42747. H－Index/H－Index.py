def solution(citations):
    answer = 0

    n=len(citations)
    citations.sort()

    for i in range(n):
        if citations[i]>=n-i:
            answer += 1

    return answer