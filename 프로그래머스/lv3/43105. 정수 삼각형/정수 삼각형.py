def solution(triangle):
    d=triangle
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                d[i][j]+=triangle[i-1][j]
            elif i==j:
                d[i][j]+=triangle[i-1][j-1]
            else:
                d[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
                
    return max(d[len(triangle)-1])
