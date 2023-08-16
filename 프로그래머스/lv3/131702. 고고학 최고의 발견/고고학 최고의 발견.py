from itertools import product
dx=[0,0,0,1,-1]
dy=[0,1,-1,0,0]

def solution(clockHands):
    answer=int(1e9)
    
    n=len(clockHands)
    
    def calc(x,y):
        temp=0
        for d in range(5):
            nx,ny = x+dx[d], y+dy[d]
            if 0<=nx<n and 0<=ny<n:
                temp+=data[nx][ny]
        return (clockHands[x][y]+temp)%4

    
    for li in product(range(4), repeat=n):
        data=[[0]*n for _ in range(n)]
        data[0]=list(li).copy() # 첫째행
        
        for i in range(1,n):
            for j in range(n):
                data[i][j]=(4-calc(i-1,j))%4
                
        for i in range(n):
            if calc(n-1, i) !=0:
                break
        else:
            temp=sum([sum(t) for t in data])
            answer= min(answer, temp)
                

    return answer
