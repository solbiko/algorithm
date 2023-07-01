def solution(N, stages):
    result = {}
    a = len(stages)
    for i in range(1,N+1):
        if a != 0:
            cnt = stages.count(i) # stages에서 i의 개수
            result[i] = cnt/a
            a-=cnt
        else:
            result[i] = 0

    return sorted(result, key=lambda x: result[x], reverse=True)


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))