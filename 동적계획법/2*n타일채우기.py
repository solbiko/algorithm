# 2*n크기 직사각형을 2*1/1*n으로 채우는 방법의 수
n = int(input())

d= [0]*(n+1)
d[1]=1
d[2]=2
for i in range(3, n+1):
    d[i]= d[i-1]+d[i-2]

print(d)
print(d[n]% 10007)