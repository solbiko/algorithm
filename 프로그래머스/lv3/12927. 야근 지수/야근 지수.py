from heapq import heapify, heappush, heappop
def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]

    heapify(works) # 최대힙

    while n > 0:
        maxval = heappop(works)
        heappush(works, maxval+1)
        n -= 1

    for w in works:
        answer += w**2

    return answer