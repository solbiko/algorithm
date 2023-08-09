from itertools import combinations
def solution(line):
    
    points=[] # 교점
    for l1, l2 in combinations(line,2):
        x1, y1, c1 = l1 # 직선1
        x2, y2, c2 = l2 # 직선2

        if x1*y2 != y1*x2: # 기울기 다름
            # 두 직선의 해
            x = (y1*c2-c1*y2)/(x1*y2-y1*x2)
            y = (c1*x2-x1*c2)/(x1*y2-y1*x2)

            # 두 직선의 해 x, y가 모두 정수라면 반환
            if x == int(x) and y == int(y):
                points.append([int(x), int(y)])
    
    
    ws,we = min(points, key = lambda x : x[0])[0], max(points, key = lambda x : x[0])[0]+1
    hs,he = min(points, key = lambda x : x[1])[1], max(points, key = lambda x : x[1])[1]+1
    
    # 모든 별을 포함하는 최소 사각형 배열
    answer = [['.']*(we-ws) for _ in range(he-hs)]
    for x, y in points:
        answer[y-hs][x-ws] = '*'
    answer.reverse()
    

    return [''.join(i) for i in answer]

