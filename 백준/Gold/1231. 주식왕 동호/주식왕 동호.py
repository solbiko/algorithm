import sys
input=sys.stdin.readline

c,d,m=map(int, input().split())
a=[]
for _ in range(c):
    a.append(list(map(int,input().split())))

for j in range(1,d):  # 날짜
    cache=[0]*(m+1)
    for i in range(c): # 주식
        now=a[i][j]
        pre=a[i][j-1] # 같은주식 전날 값
        for k in range(a[i][j-1],m+1):
            cache[k] = max(cache[k], cache[k-pre]+now-pre)
    m += cache[m]

print(m)
