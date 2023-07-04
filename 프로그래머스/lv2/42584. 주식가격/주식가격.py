from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []

    while q:
        n = q.popleft()
        t=0
        for i in q:
            t+=1
            if n>i:
                break
        answer.append(t)

    return answer