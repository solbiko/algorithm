n,k=map(int,input().split())

b=[1]*(n+1)
for i in range(1,n+1):
    b[i]=b[i-1]*(n+1-i)//i

print(b[k]%10007)
