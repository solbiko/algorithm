from heapq import heappush, heappop

def solution(scoville, K):
    cnt=0

    h=[]
    for x in scoville:
        heappush(h,x)

    while h:
        now=heappop(h)

        if now<K:
            if len(h)<1:
                return -1
            else:
                sec=heappop(h)
                heappush(h,now+sec*2)
                cnt+=1
        else: return cnt
