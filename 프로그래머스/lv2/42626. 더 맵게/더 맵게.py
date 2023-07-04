from heapq import heapify, heappush, heappop

def solution(scoville, K):
    cnt=0

    heapify(scoville)

    while True:
        now=heappop(scoville)
        if now>=K:
            break
        if len(scoville)<1:
            return -1
        sec=heappop(scoville)
        heappush(scoville,now+sec*2)
        cnt+=1
    return cnt
