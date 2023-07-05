from heapq import heappush, heappop

def solution(jobs):
    answer=0

    h=[]

    pre=-1 # 직전 종료 시각
    i=0 # 현재 시각

    cnt=0 # 처리개수
    while cnt<len(jobs):

        for job in jobs:
            if pre < job[0] <= i:
                heappush(h, [job[1], job[0]]) # (소요시간, 요청시간)

        if h:
            cur=heappop(h)
            pre=i
            i+=cur[0]
            answer+=i-cur[1]

            cnt+=1
        else:
            i+=1

    return answer//len(jobs)