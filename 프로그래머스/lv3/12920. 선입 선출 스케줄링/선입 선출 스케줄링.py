def solution(n,cores):
    answer=0

    if n <= len(cores):
        return n
    n -= len(cores)
    
    l = 1
    r = max(cores)*n

    while l < r:
        mid = (l+r)//2
        work = 0
        for core in cores:
            work += mid//core

        if work >= n:
            r=mid
        else:
            l=mid+1

    #찾아낸 (r-1) 까지의 총 작업수를 n에서 뺌
    n -= sum(map(lambda x: (r-1)//x, cores))
    # 남아있는 작업 수는 전부 현재 시간(r) 안에서 이루어짐


    for i in range(len(cores)): # r이 i의 약수 일 때 n-=1
        if r%cores[i]==0:
            n-=1
            if n==0:
                answer=i+1

    return answer
            