"""
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.
3
1 3 5
5
2 3 6 7 9

1 2 3 3 5 6 7 9
"""
n=int(input())
nlist=list(map(int,input().split()))
m=int(input())
mlist=list(map(int,input().split()))

a=nlist+mlist
a.sort()
for i in range(len(a)):
    print(a[i], end=" ")