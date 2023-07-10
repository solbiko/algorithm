import sys,math

# 점과 점 사이의 거리 구하는 함수
def dist(x1, y1, x2, y2):
    result = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    return result

def solution(m, n, startX, startY, balls):
    answer=[]
    for endX, endY in balls:
        minval=sys.maxsize
         
        # 일직선으로 공이 먼저 부딪히는 경우 빼고 계산
        
        if not (startX==endX and startY<endY): # 상
            minval = min(minval, dist(startX, 2*n-startY, endX, endY))
            
        if not (startX==endX and startY>endY): # 하
            minval = min(minval, dist(startX, -startY, endX, endY))
            
        if not (startY==endY and startX>endX): # 좌
            minval = min(minval, dist(-startX, startY, endX, endY))
            
        if not (startY==endY and startX<endX): # 우
            minval = min(minval, dist(2*m-startX, startY, endX, endY))
        
        answer.append(round(math.pow(minval,2)))

    return answer