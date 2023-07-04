"""
입국심사대는 총 N, 상근이와 친구들은 총 M
k번 심사대에 앉아있는 심사관이 한 명을 심사를 하는데 드는 시간은 Tk

상근이와 친구들이 심사를 받는데 걸리는 시간의 최솟값
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ M ≤ 1,000,000,000)
다음 N개 줄에는 각 심사대에서 심사를 하는데 걸리는 시간인 Tk가 주어진다. (1 ≤ Tk ≤ 109)
2 6
7
10
"""
n,m=map(int, input().split())
a=[]
for _ in range(n):
    a.append(int(input()))

res=0

l=1
r=max(a)*m

while l<=r:
    mid=(l+r)//2

    temp=0
    for i in a:
        temp+=mid//i
    if temp>=m:
        res=mid
        r=mid-1
    else:
        l=mid+1


print(res)