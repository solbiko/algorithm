import itertools as it
import sys
input=sys.stdin.readline

n,f=map(int,input().split())
visited=[False]*(n+1)
p=[0]*n

# 이항계수
b=[1]*n
for i in range(1,n):
    b[i]=b[i-1]*(n-i)//i

# 순열 구하기
a=list(range(1,n+1))
for tmp in it.permutations(a):
    sum=0
    for l,x in enumerate(tmp):
        sum+=x*b[l]
    if sum==f:
        for i in tmp:
            print(i, end=" ")
        print()