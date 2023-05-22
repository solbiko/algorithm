"""
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.
3
1 3 5
5
2 3 6 7 9

1 2 3 3 5 6 7 9
"""
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

c=[]
p1=p2=0


while p1<n and p2<m:
    if a[p1]<b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

# 끝까지 못가고 남음
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]

for i in c:
    print(i, end=" ")