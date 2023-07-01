def solution(cacheSize, cities):
    answer=0

    if cacheSize == 0:
        return len(cities)*5

    q=[]

    for x in cities:
        x = x.upper()
        if x in q:
            answer += 1
            q.remove(x)
            q.append(x)
        else:
            answer += 5
            if len(q) < cacheSize:
                q.append(x)
            else:
                q.pop(0)
                q.append(x)
    return answer



# print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution( 2,["Jeju", "Pangyo", "NewYork", "newyork"]))